document.addEventListener("DOMContentLoaded", function() {
    let typField = document.querySelector("#id_typ");
    let colorField = document.querySelector("#id_color");  // pokud máš barvu
    let previewImg = document.querySelector("#jacket-preview");

    function updatePreview() {
        // Pokud není vybrán typ, schováme obrázek
        if (!typField.value) {
            previewImg.style.display = "none";
            previewImg.removeAttribute("src"); // zrušíme src, aby se neukazovala ikonka
            return;
        }
        // Nastavíme src podle vybraného typu
        previewImg.src = `/static/bundy/${typField.value}.png`;
        // Pokud máš i barvu, nastav pozadí:
        previewImg.parentElement.style.backgroundColor = colorField ? colorField.value : '#f0f0f0';
        // Zobrazíme obrázek
        previewImg.style.display = "block";
    }

    if (typField) {
        typField.addEventListener("change", updatePreview);
    }
    if (colorField) {
        colorField.addEventListener("input", updatePreview);
    }
});
