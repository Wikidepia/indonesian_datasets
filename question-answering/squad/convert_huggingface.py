import json

with open("train-v2.0.json") as f:
    content = json.load(f)

hf_data = []
for data in content["data"]:
    title = data["title"]
    for paragraph in data["paragraphs"]:
        context = paragraph["context"]
        for qa in paragraph["qas"]:
            fill = {
                "id":  qa["id"],
                "title": title,
                "context": context,
                "question": qa["question"],
                "answers": {"answer_start": [], "text": []}
            }
            answers = qa["plausible_answers"] if qa["is_impossible"] else qa["answers"]
            for answer in answers:
                fill["answers"]["answer_start"].append(answer["answer_start"])
                fill["answers"]["text"].append(answer["text"])

            hf_data.append(fill)

with open("hf_train-v2.0.json", "w") as f:
    json.dump({"data": hf_data}, f)