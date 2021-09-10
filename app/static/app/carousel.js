// Controls the carousel animation. It's just adding/removing an 'active' class on the thumbnails and changing the src of the main image.

let active_images = document.getElementsByClassName('active');

let thumbnail_images = document.getElementsByClassName('thumbnail');

thumbnail_images[0].classList.add('active');

for (var i = 0; i < thumbnail_images.length; i++) {

    thumbnail_images[i].addEventListener('mouseover', function () {

        if (active_images.length > 0) {
            active_images[0].classList.remove('active');
        }

        this.classList.add('active');

        document.getElementById('main-image').src = this.src;
    })
}
