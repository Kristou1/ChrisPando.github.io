<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portfolio Cybersécurité</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Roboto', sans-serif;
      margin: 0;
      padding: 0;
      background-image: url('https://img.freepik.com/vecteurs-premium/fond-rouge-noir-cadenas-circuit-imprime-mot-cybersecurite-dessus_42077-16537.jpg');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      height: 100vh;
      color: #fff;
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }

    header {
      text-align: center;
      padding: 20px;
      background-color: rgba(0, 0, 0, 0.5);
    }

    h1 {
      font-size: 36px;
      margin: 0;
    }

    section {
      margin: 20px auto;
      padding: 20px;
      background-color: rgba(0, 0, 0, 0.7);
      border-radius: 8px;
      max-width: 800px;
    }

    h2 {
      color: #fff;
      font-size: 28px;
      text-align: center;
    }

    p, ul {
      font-size: 18px;
      line-height: 1.6;
      margin-bottom: 20px;
      text-align: center;
    }

    a {
      color: #e74c3c;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    /* Style pour le contenu déroulant */
    .content-hidden {
      display: none;
      max-height: 300px; /* Hauteur maximale avec défilement */
      overflow-y: auto; /* Ajoute une réglette si nécessaire */
      background-color: rgba(0, 0, 0, 0.8);
      padding: 10px;
      border-radius: 8px;
    }

    button {
      background-color: #e74c3c;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    button:hover {
      background-color: #c0392b;
    }
  </style>
</head>
<body>
  <header>
    <h1>Bienvenue sur mon Portfolio en Cybersécurité</h1>
    <p>Je suis <strong>PANDOSY Christophe</strong>, un passionné de cybersécurité en reconversion. Ce portfolio présente mes compétences, mes projets et mon parcours.</p>
  </header>

  <!-- Section À propos -->
  <section id="about">
    <h2>À propos de moi</h2>
    <p>Avec un intérêt croissant pour la sécurité des systèmes d'information, j'ai décidé de me reconvertir dans la cybersécurité après plusieurs années en tant que comptable.</p>
    <p>J'ai acquis des compétences clés comme l'analyse des vulnérabilités, la gestion des incidents de sécurité, et la mise en place de solutions de sécurité.</p>
  </section>

  <!-- Section Certifications avec un bouton pour afficher/masquer le contenu -->
  <section id="certifications">
    <h2>Mes certifications <button onclick="toggleContent('certifications-content')">Cliquer ici</button></h2>
    <div id="certifications-content" class="content-hidden">
      <p>Août 2023 - Certification TOSA Cybercitizen.</p>
      <p>Août 2023 - Certification TOSA DigComp.</p>
      <!-- Ajoutez d'autres certifications si nécessaire -->
    </div>
  </section>
  
  <!-- Section Projets avec un bouton pour afficher/masquer le contenu -->
  <section id="projects">
    <h2>Mes Projets <button onclick="toggleContent('projects-content')">Cliquer ici</button></h2>
    <div id="projects-content" class="content-hidden">
      <ul>
        <li><a href="Scanner_de_ports.html" target="_blank" rel="noopener noreferrer">Projet 1 : Scanner de ports</a></li>
        <li><a href="ScannerVulnWeb.html" target="_blank" rel="noopener noreferrer">Projet 2 : Scanner de vulnérabilités web</a></li>
        <li><a href="Pentest_perso.html" target="_blank" rel="noopener noreferrer">Projet 3 : Script de pentest personnalisé</a></li>
        <li><a href="Hash_Cracker.html" target="_blank" rel="noopener noreferrer">Projet 4 : Cracker de Hash</a></li>
        <!-- Ajoutez d'autres projets si nécessaire -->
      </ul>
    </div>
  </section>

  <script>
    // Fonction pour afficher/masquer le contenu
    function toggleContent(id) {
      const content = document.getElementById(id);
      if (content.style.display === 'block') {
        content.style.display = 'none';
      } else {
        content.style.display = 'block';
      }
    }
  </script>
</body>
</html>
