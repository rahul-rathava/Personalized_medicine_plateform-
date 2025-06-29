from flask import Flask, request, render_template, jsonify, send_file
import os
import json
import csv

app = Flask(__name__, template_folder='templates')

def parse_vcf(file_text):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    variants = []
    disease_risks = []
    drug_responses = []
    treatments = []
    biomarkers = []

    lines = file_text.strip().split("\n")
    for line in lines:
        if line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 5:
            continue
        ref = parts[3]
        alt = parts[4]
        variants.append(f"{ref}>{alt}")

        # Count nucleotides
        counts[ref] = counts.get(ref, 0) + 1
        counts[alt] = counts.get(alt, 0) + 1

        # Sample conditions
        if ref == "G" and alt == "A":
            disease_risks.append("Risk of Disease A")
            biomarkers.append("Gene G mutation → Biomarker X")
        if ref == "C" and alt == "T":
            disease_risks.append("Predisposition to Disease B")
            biomarkers.append("C>T → Possible marker for Disease B")
        if ref == "A" and alt == "T":
            drug_responses.append("A>T → Poor response to Drug X")
            treatments.append("Try alternative to Drug X")
        if ref == "T" and alt == "G":
            drug_responses.append("T>G → Good response to Drug Z")
            treatments.append("Consider Drug Z as primary treatment")
        if ref == "C" and alt == "G":
            drug_responses.append("C>G → Adverse reaction to Drug Y")
            treatments.append("Avoid Drug Y due to adverse reaction")

    total = sum(counts.values())
    return counts, total, variants, disease_risks, drug_responses, treatments, biomarkers


@app.route('/')
def home():
    return render_template("index.html",
                           counts={'A': '-', 'T': '-', 'G': '-', 'C': '-'},
                           total='-',
                           variants=[],
                           risks=[],
                           drug_responses=[],
                           treatments=[],
                           biomarkers=[],
                           clinical_notes={})


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        file = request.files.get('file')
        filename = file.filename.lower()
        clinical_data = request.form.get('clinical_notes')
        clinical_notes = {}

        if clinical_data:
            try:
                clinical_notes = json.loads(clinical_data)
            except Exception:
                clinical_notes = {"error": "Invalid clinical JSON"}

        if filename.endswith('.vcf'):
            genome_text = file.read().decode('utf-8')
            counts, total, variants, risks, drug_responses, treatments, biomarkers = parse_vcf(genome_text)

            # Save JSON
            result_json = {
                "counts": counts,
                "total": total,
                "variants": variants,
                "disease_risks": risks,
                "drug_predictions": drug_responses,
                "treatments": treatments,
                "biomarkers": biomarkers,
                "clinical_notes": clinical_notes
            }
            with open("analysis_result.json", "w") as jf:
                json.dump(result_json, jf, indent=4)

            # Save CSV (basic counts only)
            with open("analysis_result.csv", "w", newline='') as cf:
                writer = csv.writer(cf)
                writer.writerow(["A", "T", "G", "C", "Total"])
                writer.writerow([counts['A'], counts['T'], counts['G'], counts['C'], total])

            # Response
            if request.headers.get("Accept") == "application/json" or request.user_agent.string.startswith("Python"):
                return jsonify({"result": result_json})

            return render_template("index.html",
                                   counts=counts,
                                   total=total,
                                   variants=variants,
                                   risks=risks,
                                   drug_responses=drug_responses,
                                   treatments=treatments,
                                   biomarkers=biomarkers,
                                   clinical_notes=clinical_notes)

        elif filename.endswith('.bam'):
            return jsonify({"message": "✅ Received BAM file. Parsing logic will be implemented."})

        elif filename.endswith('.fastq'):
            return jsonify({"message": "✅ Received FASTQ file. Parsing logic will be implemented."})

        else:
            return jsonify({"message": "❌ Unsupported file format"}), 400

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"message": f"❌ Genome analysis failed: {str(e)}"}), 500


@app.route('/download/json')
def download_json():
    return send_file("analysis_result.json", as_attachment=True)


@app.route('/download/csv')
def download_csv():
    return send_file("analysis_result.csv", as_attachment=True)


if __name__ == '__main__':
    app.run(port=5006)
