export default function show_image(src) {
	console.log('hi');
	var img = document.createElement("img");
	img.src = src;
	document.appendChild(img);	
}
