// Modal Functions
function openModalLogout() {
    const modal = document.getElementById('modalLogout');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModalLogout() {
    const modal = document.getElementById('modalLogout');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

function openModalAddClient() {
    const modal = document.getElementById('modalAddClient'); 
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModalAddClient() {
    const modal = document.getElementById('modalAddClient');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

function openModalEditClient(id, nom, sexe, telephone, adresse) {

    const modal = document.getElementById("modalAddClient");

    // ✅ Même logique que openModalAddClient
    modal.classList.add("active");
    document.body.style.overflow = "hidden";

    // Remplit les champs
    document.getElementById("client_id").value = id;
    document.getElementById("id_nom_prenom").value = nom;
    document.getElementById("id_sexe").value = sexe;
    document.getElementById("id_telephone").value = telephone;
    document.getElementById("id_adresse").value = adresse;

    // Change le titre
    document.querySelector(".modal-title").innerText = "Modifier le/la client(e)";
}

function openModalDeleteClient(id, nom) {
    const modal = document.getElementById('modalDeleteClient');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Mettre à jour le message
    const msg = document.getElementById('deleteClientMessage');
    msg.innerText = `Êtes-vous sûr de vouloir supprimer ${nom} ?`;

    // Mettre à jour le lien
    const link = document.getElementById('deleteClientLink');
    link.href = `supprimer/${id}/`;  // Remplace par ton URL correcte
}

function closeModalDeleteClient() {
    const modal = document.getElementById('modalDeleteClient');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}




// On récupère juste le chemin de base de la page actuelle
// ex: /dashboard/depenses/
const BASE = "/dashboard/depenses/";

function openModalAdd() {
    document.getElementById('modalAddTitle').innerText = 'Nouvelle dépense';
    document.getElementById('depenseForm').action = BASE;
    document.getElementById('depense_id').value = '';
    document.getElementById('id_motif').value = '';
    document.getElementById('id_montant').value = '';
    document.getElementById('modalAdd').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModalAdd() {
    document.getElementById('modalAdd').classList.remove('active');
    document.body.style.overflow = 'auto';
}

function openModalEdit(id, motif, montant) {
    document.getElementById('modalAddTitle').innerText = 'Modifier la dépense';
    document.getElementById('depenseForm').action = BASE + 'modifier/' + id + '/';
    document.getElementById('depense_id').value = id;
    document.getElementById('id_motif').value = motif;
    document.getElementById('id_montant').value = montant;
    document.getElementById('modalAdd').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function openModalDelete(id, motif) {
    document.getElementById('deleteMessage').innerText =
        `Êtes-vous sûr de vouloir supprimer "${motif}" ?`;
    document.getElementById('deleteLink').href = BASE + 'supprimer/' + id + '/';
    document.getElementById('modalDelete').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModalDelete() {
    document.getElementById('modalDelete').classList.remove('active');
    document.body.style.overflow = 'auto';
}



function openModalAddCommand() {
    const modal = document.getElementById('modalAddCommand');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function openModalEditCommand(id, nom, date_livraison, montant, avance, statut) {

    const modal = document.getElementById("modalAddCommand");

    // ✅ Même logique que openModalAddCommand
    modal.classList.add("active");
    document.body.style.overflow = "hidden";

    // Remplit les champs
    document.getElementById("command_id").value = id;
    document.getElementById("id_client").value = nom;
    document.getElementById("id_date_livraison").value = date_livraison;
    document.getElementById("id_montant").value = montant;
    document.getElementById("id_avance").value = avance;
    document.getElementById("id_statut").value = statut;

    // Change le titre
    document.querySelector(".modal-title").innerText = "Modifier la commande";
}


function openModalDeleteCommand(id, nom) {
    const modal = document.getElementById('modalDeleteCommand');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Mettre à jour le message
    const msg = document.getElementById('deleteCommandMessage');
    msg.innerText = `Êtes-vous sûr de vouloir supprimer la commande de ${nom} ?`;

    // Mettre à jour le lien
    const link = document.getElementById('deleteCommandLink');
    link.href = `supprimer/${id}/`;  // Remplace par ton URL correcte
}

function closeModalDeleteCommand() {
    const modal = document.getElementById('modalDeleteCommand');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}


function closeModalAddCommand() {
    const modal = document.getElementById('modalAddCommand');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}



function openModalAddMesureFemme() {
    const modal = document.getElementById('modalAddMesureFemme'); 
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModalAddMesureFemme() {
    const modal = document.getElementById('modalAddMesureFemme');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

function openModalMesureFemme(modalId) {
    document.getElementById(modalId).style.display = 'flex'; // ou 'block' selon votre CSS
}

function closeModalMesureFemme(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Fermer en cliquant sur l'overlay (optionnel)
document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', function(e) {
        if (e.target === this) {
            this.style.display = 'none';
        }
    });
});


function openModalDeleteMesureFemme(id) {
    const modal = document.getElementById('modalDeleteMesureFemme');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Mettre à jour le message
    const msg = document.getElementById('deleteMesureFemmeMessage');
    msg.innerText = `Êtes-vous sûr de vouloir supprimer ?`;

    // Mettre à jour le lien
    const link = document.getElementById('deleteMesureFemmeLink');
    link.href = `supprimer/${id}/`;  // Remplace par ton URL correcte
}

function closeModalDeleteMesureFemme() {
    const modal = document.getElementById('modalDeleteMesureFemme');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}



function openModalAddMesureHomme() {
    const modal = document.getElementById('modalAddMesureHomme'); 
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModalAddMesureHomme() {
    const modal = document.getElementById('modalAddMesureHomme');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

function openModalMesureHomme(modalId) {
    document.getElementById(modalId).style.display = 'flex'; // ou 'block' selon votre CSS
}

function closeModalMesureHomme(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

function openModalEditMesureFemme(id, client_id, epaule_dos, tour_poitrine, longueur_manche, tour_manche,
    carrure_devant, carrure_dos, longueur_sein, longueur_corsage,
    tour_taille, ceinture, tour_hanche, longueur_clotop, longueur_robe,
    longueur_jupe, longueur_chambrage_dos, longueur_bohumba, ecart_seins, longueur_pantalon,
    longueur_genou, longueur_taille_devant, longueur_taille_dos, tour_bas, tour_encolure) {

    // Remplir les champs
    document.getElementById('edit_client_id').value = client_id;
    document.getElementById('edit_epaule_dos').value = epaule_dos;
    document.getElementById('edit_tour_poitrine').value = tour_poitrine;
    document.getElementById('edit_longueur_manche').value = longueur_manche;
    document.getElementById('edit_tour_manche').value = tour_manche;
    document.getElementById('edit_carrure_devant').value = carrure_devant;
    document.getElementById('edit_carrure_dos').value = carrure_dos;
    document.getElementById('edit_longueur_sein').value = longueur_sein;
    document.getElementById('edit_longueur_corsage').value = longueur_corsage;
    document.getElementById('edit_tour_taille').value = tour_taille;
    document.getElementById('edit_ceinture').value = ceinture;
    document.getElementById('edit_tour_hanche').value = tour_hanche;
    document.getElementById('edit_longueur_clotop').value = longueur_clotop;
    document.getElementById('edit_longueur_robe').value = longueur_robe;
    document.getElementById('edit_longueur_jupe').value = longueur_jupe;
    document.getElementById('edit_longueur_chambrage_dos').value = longueur_chambrage_dos;
    document.getElementById('edit_longueur_bohumba').value = longueur_bohumba;
    document.getElementById('edit_ecart_seins').value = ecart_seins;
    document.getElementById('edit_longueur_pantalon').value = longueur_pantalon;
    document.getElementById('edit_longueur_genou').value = longueur_genou;
    document.getElementById('edit_longueur_taille_devant').value = longueur_taille_devant;
    document.getElementById('edit_longueur_taille_dos').value = longueur_taille_dos;
    document.getElementById('edit_tour_bas').value = tour_bas;
    document.getElementById('edit_tour_encolure').value = tour_encolure;

    // Définir l'action du formulaire dynamiquement
    document.getElementById('editMesureFemmeForm').action = `/clients/mesures_femmes/${id}/modifier/`;

    document.getElementById('modalEditMesureFemme').style.display = 'flex';
}

function closeModalEditMesureFemme() {
    document.getElementById('modalEditMesureFemme').style.display = 'none';
}


function openModalEditMesureHomme(id, client_id, epaule_dos, tour_poitrine, tour_manche, longueur_manche,
    longueur_bohumba, tour_cou, longueur_chemise, ceinture, tour_hanche,
    longueur_pantalon, longueur_genou, tour_genou, tour_bas, tour_cuisse,
    longueur_culotte, longueur_gilet, longueur_veste) {

    document.getElementById('edit_client_id').value = client_id;
    document.getElementById('edit_epaule_dos').value = epaule_dos;
    document.getElementById('edit_tour_poitrine').value = tour_poitrine;
    document.getElementById('edit_tour_manche').value = tour_manche;
    document.getElementById('edit_longueur_manche').value = longueur_manche;
    document.getElementById('edit_longueur_bohumba').value = longueur_bohumba;
    document.getElementById('edit_tour_cou').value = tour_cou;
    document.getElementById('edit_longueur_chemise').value = longueur_chemise;
    document.getElementById('edit_ceinture').value = ceinture;
    document.getElementById('edit_tour_hanche').value = tour_hanche;
    document.getElementById('edit_longueur_pantalon').value = longueur_pantalon;
    document.getElementById('edit_longueur_genou').value = longueur_genou;
    document.getElementById('edit_tour_genou').value = tour_genou;
    document.getElementById('edit_tour_bas').value = tour_bas;
    document.getElementById('edit_tour_cuisse').value = tour_cuisse;
    document.getElementById('edit_longueur_culotte').value = longueur_culotte;
    document.getElementById('edit_longueur_gilet').value = longueur_gilet;
    document.getElementById('edit_longueur_veste').value = longueur_veste;

    document.getElementById('editMesureHommeForm').action = `/clients/mesures_hommes/${id}/modifier/`;
    document.getElementById('modalEditMesureHomme').style.display = 'flex';
}

function closeModalEditMesureHomme() {
    document.getElementById('modalEditMesureHomme').style.display = 'none';
}

function closeModalEditMesureHomme() {
    document.getElementById('modalEditMesureHomme').style.display = 'none';
}


// Fermer en cliquant sur l'overlay (optionnel)
document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', function(e) {
        if (e.target === this) {
            this.style.display = 'none';
        }
    });
});


function openModalDeleteMesureHomme(id) {
    const modal = document.getElementById('modalDeleteMesureHomme');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Mettre à jour le message
    const msg = document.getElementById('deleteMesureHommeMessage');
    msg.innerText = `Êtes-vous sûr de vouloir supprimer ?`;

    // Mettre à jour le lien
    const link = document.getElementById('deleteMesureHommeLink');
    link.href = `supprimer/${id}/`;  // Remplace par ton URL correcte
}

function closeModalDeleteMesureHomme() {
    const modal = document.getElementById('modalDeleteMesureHomme');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}




// Close modal when clicking outside
document.getElementById('modalAddClient').addEventListener('click', (e) => {
    if (e.target.id === 'modalAddClient') {
        closeModal();
    }
});

function openModal() {
    const modal = document.getElementById('modalNouvelleCommande');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('modalNouvelleCommande');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Close modal when clicking outside
document.getElementById('modalNouvelleCommande').addEventListener('click', (e) => {
    if (e.target.id === 'modalNouvelleCommande') {
        closeModal();
    }
});

// Close modal with Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});


// Fonction pour afficher une alerte (pour la démo)
function showAlert(type) {
    const container = document.getElementById('alertContainer');
    
    const messages = {
        success: 'Opération réussie ! Votre action a été effectuée avec succès.',
        error: 'Une erreur est survenue. Veuillez réessayer.',
        warning: 'Attention ! Cette action nécessite votre confirmation.',
        info: 'Information : Votre session expire dans 5 minutes.'
    };

    const icons = {
        success: 'ri-checkbox-circle-line',
        error: 'ri-error-warning-line',
        warning: 'ri-alert-line',
        info: 'ri-information-line'
    };

    const alert = document.createElement('div');
    alert.className = `alert ${type}`;
    alert.innerHTML = `
        <button class="alert-close" onclick="closeAlert(this)">
            <i class="ri-close-line"></i>
        </button>
        <h4 class="alert-title">
            <i class="${icons[type]}"></i> TailorBook
        </h4>
        <div class="alert-message">${messages[type]}</div>
    `;

    container.appendChild(alert);

    // Auto-fermeture après 5 secondes
    setTimeout(() => {
        closeAlert(alert.querySelector('.alert-close'));
    }, 5000);
}

// Fonction pour fermer une alerte
function closeAlert(button) {
    const alert = button.parentElement;
    alert.classList.add('hiding');
    setTimeout(() => {
        alert.remove();
    }, 400);
}

// Auto-fermeture des alertes Django après 5 secondes
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const closeBtn = alert.querySelector('.alert-close');
            if (closeBtn) {
                closeAlert(closeBtn);
            }
        }, 5000);
    });
});

// Form submission
document.getElementById('formNouvelleCommande').addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Here you would normally send the data to your backend
    console.log('Form submitted');
    
    // Show success message (you can customize this)
    alert('Commande créée avec succès !');
    
    // Close modal and reset form
    closeModal();
    e.target.reset();
});


// Navigation
const navLinks = document.querySelectorAll('.nav-link');
const submenuLinks = document.querySelectorAll('.submenu-link');
const pageTitle = document.getElementById('pageTitle');

// Toggle submenu
const mesuresMenu = document.getElementById('mesuresMenu');
const mesuresLink = mesuresMenu.querySelector('.nav-link');

mesuresLink.addEventListener('click', (e) => {
    e.preventDefault();
    mesuresMenu.classList.toggle('open');
});

// Handle main nav links
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        // Don't prevent default for submenu parents
        if (!link.classList.contains('has-dropdown')) {
            e.preventDefault();
            
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            submenuLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            link.classList.add('active');
            
            // Update page title
            const pageName = link.querySelector('span').textContent;
            pageTitle.textContent = pageName;
            
            // Close sidebar on mobile
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('open');
            }
            
            // Load page content
            loadPageContent(link.dataset.page);
        }
    });
});

// Handle submenu links
submenuLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        
        // Remove active class from all links
        navLinks.forEach(l => l.classList.remove('active'));
        submenuLinks.forEach(l => l.classList.remove('active'));
        
        // Add active class to clicked submenu link and parent
        link.classList.add('active');
        mesuresLink.classList.add('active');
        
        // Update page title
        const pageName = link.querySelector('span').textContent;
        pageTitle.textContent = `Mesures ${pageName}`;
        
        // Close sidebar on mobile
        if (window.innerWidth <= 768) {
            sidebar.classList.remove('open');
        }
        
        // Load page content
        loadPageContent(link.dataset.page);
    });
});


// Handle window resize
window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        sidebar.classList.remove('open');
    }
});
