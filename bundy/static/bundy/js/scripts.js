document.addEventListener("DOMContentLoaded", function() {
    // Pro update náhledu bundy
    const typField = document.querySelector("#id_typ");
    const colorField = document.querySelector("#id_color");
    const previewImg = document.querySelector("#jacket-preview");

    function updatePreview() {
        // Pokud není vybrán typ, schováme obrázek
        if (!typField.value) {
            previewImg.style.display = "none";
            previewImg.removeAttribute("src");
            return;
        }
        // Nastavíme src podle vybraného typu
        previewImg.src = `/static/bundy/${typField.value}.png`;
        // Pokud je pole pro barvu, nastav pozadí obalu obrázku, jinak nastav výchozí
        if (colorField) {
            previewImg.parentElement.style.backgroundColor = colorField.value;
        } else {
            previewImg.parentElement.style.backgroundColor = '#f0f0f0';
        }
        // Zobrazíme obrázek
        previewImg.style.display = "block";
    }

    if (typField && previewImg) {
        typField.addEventListener("change", updatePreview);
    }
    if (colorField) {
        colorField.addEventListener("input", updatePreview);
    }

    // Pro hover efekt na Instagram odkaz
    const instagramLink = document.querySelector("footer a.instagram");
    if (instagramLink) {
        instagramLink.addEventListener("mouseenter", function() {
            document.body.classList.add("bg-easteregg");
        });
        instagramLink.addEventListener("mouseleave", function() {
            document.body.classList.remove("bg-easteregg");
        });
    }
});
