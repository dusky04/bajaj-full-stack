from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


# NAME  : Vaibhav Rastogi
# REG NO: 22BDS0131


@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.json.get("data", [])

        # classify numbers (must remain as strings)
        numbers = [x for x in data if x.isdigit()]
        odd_numbers = [x for x in numbers if int(x) % 2 != 0]
        even_numbers = [x for x in numbers if int(x) % 2 == 0]

        # alphabets
        alphabets = [x for x in data if x.isalpha()]
        alphabets_upper = [x.upper() for x in alphabets]

        # special characters (not alnum)
        special_characters = [x for x in data if not x.isalnum()]

        # sum of numbers (string form)
        total_sum = str(sum(int(x) for x in numbers))

        # concat alphabets reversed with alternating caps
        concat_string = "".join(alphabets)[::-1]
        alternating_caps_list = []
        for i, char in enumerate(concat_string):
            if i % 2 == 0:
                alternating_caps_list.append(char.upper())
            else:
                alternating_caps_list.append(char.lower())
        alternating_caps_string = "".join(alternating_caps_list)

        today_str = datetime.now().strftime("%d%m%Y")
        response = {
            "is_success": True,
            "user_id": f"vaibhav_rastogi_{today_str}",  # fullname_ddmmyyyy
            "email": "vaibhav.rastogi@example.com",
            "roll_number": "22BDS0131",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets_upper,
            "special_characters": special_characters,
            "sum": total_sum,
            "concat_string": alternating_caps_string,
        }
        print(response)
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
