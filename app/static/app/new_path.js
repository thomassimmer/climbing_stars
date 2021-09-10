// Controls the button to upload pictures when creating a new path. Just changing the label according to how many pictures are saved.

let fileInput = document.getElementById('imageUploader');

let fileInputLabel = document.getElementById('labelImageUpload')

fileInput.addEventListener('change', function (event) {
    let nbFilesUploaded = fileInput.files.length;

    fileInputLabel.textContent = String(nbFilesUploaded) + " image"
    fileInputLabel.textContent += nbFilesUploaded > 1 ? "s" : "";
    fileInputLabel.textContent += " selected.";
})