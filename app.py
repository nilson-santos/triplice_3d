from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        LINK_WHATSAPP="https://wa.me/554591080886",
        LINK_INSTAGRAM="https://www.instagram.com/triplice.3d/",
        LINK_SITE="#"
    )


@app.route("/termos")
def termos():
    return render_template(
        "termos.html",
        APP_NAME="Tríplice 3D",
        LAST_UPDATED="25 de outubro de 2025",
        COMPANY_NAME="Praia Dev LTDA",
        CONTACT_EMAIL="contato@praiadev.com",
        GOVERNING_LAW="Brasil"
    )


@app.route('/health-check')
def flask_health_check():
    return "success"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
