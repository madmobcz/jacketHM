document.addEventListener("DOMContentLoaded", function() {
    let typField = document.querySelector("#id_typ");
    let colorField = document.querySelector("#id_color");
    let previewImg = document.querySelector("#jacket-preview");

    function updatePreview() {
        let selectedType = typField.value;
        let selectedColor = colorField.value;
        if (selectedType) {
            previewImg.src = `/static/bundy/${selectedType}.png`;
            previewImg.style.display = "block";
            previewImg.style.backgroundColor = selectedColor;
        } else {
            previewImg.style.display = "none";
        }
    }

    if (typField) {
        typField.addEventListener("change", updatePreview);
    }
    if (colorField) {
        colorField.addEventListener("input", updatePreview);
    }
});
