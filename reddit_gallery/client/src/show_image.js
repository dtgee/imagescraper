function show_image() {
	var src = document.currentScript.getAttribute('path')
	add_image(src)
}

function add_image(src) {
	var img = document.createElement("img");
	img.src = src;
	document.appendChild(img);	
}
