

const mymap = L.map('map').setView([44.3202, 23.7988], 13);

const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mymap);

coords = [[44.319519, 23.801625], [44.319722,23.802012], [44.319443, 23.802418], [44.319647, 23.802590]];
names = ['Semaphore 1', 'Semaphore 2', 'Semaphore 3', 'Semaphore 4'];

var semaphore1 = document.querySelector('#semaphore1');
var semaphore2 = document.querySelector('#semaphore2');
var semaphore3 = document.querySelector('#semaphore3');
var semaphore4 = document.querySelector('#semaphore4');

semaphores = [semaphore1, semaphore2, semaphore3, semaphore4, semaphore4];

for(let i=0; i<coords.length; i++){
    //popup
    var pop = L.popup({
        closeOnClick: true
    }).setContent('Semaphore ' + (i+1).toString());

    //markers
    var marker = L.marker(coords[i]).addTo(mymap).bindPopup(pop);


    // labels
    /*
    var tooltip = L.tooltip({
        permanent: true
    }).setContent(names[i]);
    marker.bindTooltip(tooltip);
    */

    semaphores[i].addEventListener("mouseover", ()=> {
        mymap.flyTo(coords[i], 17);
    });
}
/*
const circle = L.circle([44.3202, 23.7988], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);
*/



