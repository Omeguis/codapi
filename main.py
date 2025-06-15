from flask import Flask, jsonify

app = Flask(__name__)

# Weapons data
weapons = {
    "uzi": {
        "name": "Uzi",
        "type": "SMG",
        "attachments": {
            "silencer": {
                "name": "Silencer",
                "effect": "Reduces weapon noise"
            }
        }
    },
    "ak47": {
        "name": "AK-47",
        "type": "Assault Rifle",
        "attachments": {
            "silencer": {
                "name": "Silencer",
                "effect": "Reduces weapon noise"
            }
        }
    },
    "fal": {
        "name": "FAL",
        "type": "Battle Rifle",
        "attachments": {
            "silencer": {
                "name": "Silencer",
                "effect": "Reduces weapon noise"
            }
        }
    }
}

@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/weapons')
def get_weapons():
    return jsonify(weapons)

@app.route('/weapons/<weapon_id>')
def get_weapon(weapon_id):
    if weapon_id.lower() in weapons:
        return jsonify(weapons[weapon_id.lower()])
    return jsonify({"error": "Weapon not found"}), 404

@app.route('/weapons/<weapon_id>/attachments')
def get_weapon_attachments(weapon_id):
    if weapon_id.lower() in weapons:
        return jsonify(weapons[weapon_id.lower()]["attachments"])
    return jsonify({"error": "Weapon not found"}), 404

@app.route('/weapons/<weapon_id>/attachments/<attachment_id>')
def get_weapon_attachment(weapon_id, attachment_id):
    if weapon_id.lower() in weapons:
        if attachment_id.lower() in weapons[weapon_id.lower()]["attachments"]:
            return jsonify(weapons[weapon_id.lower()]["attachments"][attachment_id.lower()])
        return jsonify({"error": "Attachment not found"}), 404
    return jsonify({"error": "Weapon not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 