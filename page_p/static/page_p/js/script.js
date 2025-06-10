// Ajoutez ici votre logique JavaScript pour les interactions avec l'interface utilisateur
// Par exemple, vous pouvez ajouter des événements pour les clics sur les liens de navigation.

// Fonction de défilement en douceur vers une section spécifique
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: "smooth" });
}

// Attachez des événements de clic aux liens de navigation
const navLinks = document.querySelectorAll("nav a");
navLinks.forEach(link => {
    link.addEventListener("click", event => {
        event.preventDefault(); // Empêchez le lien de recharger la page
        const sectionId = link.getAttribute("href");
        scrollToSection(sectionId);
    });
});