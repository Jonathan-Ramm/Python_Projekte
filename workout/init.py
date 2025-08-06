from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Trainingsplan: Brust, Core & Oberkörper", 0, 1, "C")
        self.ln(5)

    def chapter_title(self, num, label):
        self.set_font("Arial", "B", 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, f"Tag {num}: {label}", 0, 1, "L", 1)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 8, body)
        self.ln()

def main():
    pdf = PDF()
    pdf.add_page()

    intro = (
        "Dieser Trainingsplan fokussiert primär Brustmuskulatur und Core, "
        "bezieht aber auch Ober- und Unterarme sowie andere Oberkörpermuskeln mit ein. "
        "Du hast eine Hantel (2, 5, 7.5, 10 kg) und läufst montags und freitags joggen für den Kreislauf. "
        "Kalorienziel für Muskelaufbau: ca. 2500 kcal täglich (via Yazio).\n\n"
        "Wichtig: Zwischen den Sätzen 60-90 Sekunden Pause machen, um ausreichend zu regenerieren."
    )
    pdf.chapter_body(intro)

    pdf.chapter_title(1, "Montag")
    pdf.chapter_body("Joggen gehen")

    # Dienstag: Brust + Core + Oberkörper
    dienstag_text = (
        "- Liegestütze (verschiedene Varianten: klassisch, breit, eng) - 4 Sätze x 10-15 Wiederholungen\n"
        "  Pause: 60-90 Sekunden zwischen den Sätzen\n"
        "- Hantel-Bankdrücken (auf dem Boden liegend) - 4 Sätze x 8-12 Wiederholungen\n"
        "  Pause: 60-90 Sekunden\n"
        "- Plank (Unterarmstütz) - 3 Sätze, jeweils 30-60 Sekunden halten\n"
        "  Pause: 30-60 Sekunden\n"
        "- Seitstütz (je Seite) - 3 Sätze x 30 Sekunden\n"
        "  Pause: 30-60 Sekunden\n"
        "- Bizeps-Curls mit Hantel - 3 Sätze x 10-12 Wiederholungen\n"
        "  Pause: 60 Sekunden\n"
        "- Trizeps-Kickbacks mit Hantel - 3 Sätze x 10-12 Wiederholungen\n"
        "  Pause: 60 Sekunden\n"
        "- Schulterheben (Shrugs) mit Hantel - 3 Sätze x 12-15 Wiederholungen\n"
        "  Pause: 60 Sekunden"
    )
    pdf.chapter_title(2, "Dienstag")
    pdf.chapter_body(dienstag_text)

    pdf.chapter_title(3, "Mittwoch")
    pdf.chapter_body("Pause / Erholung")

    # Donnerstag: Core & Oberkörper Fokus
    donnerstag_text = (
        "- Russian Twists (mit Hantel) - 3 Sätze x 20 Wiederholungen (10 pro Seite)\n"
        "  Pause: 30-60 Sekunden\n"
        "- Beinheben liegend - 3 Sätze x 12-15 Wiederholungen\n"
        "  Pause: 30-60 Sekunden\n"
        "- Superman-Hold - 3 Sätze x 30 Sekunden\n"
        "  Pause: 30 Sekunden\n"
        "- Schulterdrücken mit Hantel - 3 Sätze x 8-12 Wiederholungen\n"
        "  Pause: 60-90 Sekunden\n"
        "- Hantelrudern einarmig - 3 Sätze x 10-12 Wiederholungen pro Seite\n"
        "  Pause: 60 Sekunden\n"
        "- Hammer-Curls (neutraler Griff) - 3 Sätze x 10-12 Wiederholungen\n"
        "  Pause: 60 Sekunden"
    )
    pdf.chapter_title(4, "Donnerstag")
    pdf.chapter_body(donnerstag_text)

    pdf.chapter_title(5, "Freitag")
    pdf.chapter_body("Joggen gehen")

    # Samstag: Ganzkörper leichtes Krafttraining
    samstag_text = (
        "- Liegestütze - 3 Sätze x 12-15 Wiederholungen\n"
        "  Pause: 60 Sekunden\n"
        "- Hantel-Sumo-Kniebeuge - 3 Sätze x 12 Wiederholungen\n"
        "  Pause: 60-90 Sekunden\n"
        "- Plank - 3 Sätze x 45 Sekunden\n"
        "  Pause: 30-60 Sekunden\n"
        "- Bizeps- und Trizeps Supersatz mit Hantel (je 3 Sätze x 10 Wiederholungen)\n"
        "  Pause: 60 Sekunden\n"
        "- Schulterkreisen mit Hantel - 3 Sätze x 15 pro Richtung\n"
        "  Pause: 30 Sekunden"
    )
    pdf.chapter_title(6, "Samstag")
    pdf.chapter_body(samstag_text)

    pdf.chapter_title(7, "Sonntag")
    pdf.chapter_body("Pause / Erholung")

    pdf.output("Trainingsplan.pdf")

if __name__ == "__main__":
    main()
