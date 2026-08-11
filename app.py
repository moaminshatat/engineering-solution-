from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="description" content="Civil Engineering, GIS, Water Resources, Infrastructure Engineering and Sustainable Land Management services in Belgium.">
    <meta name="keywords" content="Civil Engineer, GIS, Water Resources, Infrastructure Engineering, AutoCAD, Civil 3D, Belgium, Sustainable Land Management">
    <meta name="author" content="Momin Azmi Shatat">
    <meta name="google-site-verification" content="Oem5iuWD0GKJOIvOnkEaS8W6Ar3YDHxgALnrojAm0HM">

    <title>Momin Engineering Solutions</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f4f6f9;
            color: #333;
        }

        nav {
            background: #0F4C81;
            color: white;
            padding: 20px 50px;
        }

        .hero {
            background:
                linear-gradient(rgba(15,76,129,0.85), rgba(15,76,129,0.85)),
                url('https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=1200&q=80');

            background-size: cover;
            background-position: center;
            color: white;
            text-align: center;
            padding: 120px 20px;
        }

        .hero h1 {
            font-size: 50px;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 22px;
        }

        .section {
            padding: 60px 10%;
        }

        .section h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #0F4C81;
        }

        .about,
        .contact {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            line-height: 1.8;
        }

        .services {
            display: flex;
            flex-wrap: wrap;
            gap: 25px;
            justify-content: center;
        }

        .card {
            background: white;
            width: 300px;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }

        .card h3 {
            color: #0F4C81;
            margin-bottom: 15px;
        }

        footer {
            background: #222;
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
</head>

<body>

<nav>
    <h2>Momin Engineering Solutions</h2>
</nav>

<section class="hero">
    <h1>Civil Engineering & Sustainable Land Management</h1>
    <p>Infrastructure • Water Systems • GIS • Project Management</p>
</section>

<section class="section">
    <h2>About Me</h2>

    <div class="about">
        <p>Welcome to Momin Engineering Solutions.</p>

        <p>
            I am Momin Azmi Shatat, a Civil Engineer and MSc student
            in Sustainable Land Management at Vrije Universiteit Brussel.
        </p>

        <p>
            My experience includes infrastructure projects,
            excavation works, utility installation,
            asphalt paving coordination, site supervision,
            and engineering education.
        </p>
    </div>
</section>

<section class="section">
    <h2>Professional Services</h2>

    <div class="services">

        <div class="card">
            <h3>Infrastructure Engineering</h3>
            <p>Site supervision, utilities installation, and construction management.</p>
        </div>

        <div class="card">
            <h3>GIS & Remote Sensing</h3>
            <p>Spatial analysis using QGIS and Google Earth Engine.</p>
        </div>

        <div class="card">
            <h3>Project Planning</h3>
            <p>Scheduling and project control using Primavera and engineering tools.</p>
        </div>

        <div class="card">
            <h3>Hydraulics & Water Systems</h3>
            <p>Engineering analysis and design related to water resources.</p>
        </div>

        <div class="card">
            <h3>AutoCAD & Civil 3D</h3>
            <p>Technical drawings and engineering design solutions.</p>
        </div>

        <div class="card">
            <h3>Sustainable Land Management</h3>
            <p>Environmental and sustainable development solutions.</p>
        </div>

    </div>
</section>

<section class="section">
    <h2>Contact Information</h2>

    <div class="contact">
        <p><strong>Name:</strong> Momin Azmi F. Shatat</p>
        <p><strong>Email:</strong> mominshatat@gmail.com</p>
        <p><strong>Phone:</strong> +32 467 63 56 09</p>
        <p><strong>Location:</strong> Gent, Belgium</p>
    </div>
</section>

<footer>
    © 2026 Momin Engineering Solutions
</footer>

</body>
</html>
"""


@app.route("/robots.txt")
def robots():
    return Response(
        """User-agent: *
Allow: /

Sitemap: https://engineering-solution.onrender.com/sitemap.xml
""",
        mimetype="text/plain"
    )


@app.route("/sitemap.xml")
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://engineering-solution.onrender.com/</loc>
        <priority>1.0</priority>
    </url>
</urlset>
"""
    return Response(xml, mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)
