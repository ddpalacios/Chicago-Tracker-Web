function open_map() {
    var chicago_map = L.map('mapid').setView([41.8781, 87.6298], 10);
    var link = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: link
    }).addTo(chicago_map);
    set_marker(chicago_map);
    send_data();

}



function set_marker(chicago_map) {
    L.marker([41.73206, -87.62463]).addTo(chicago_map).bindPopup('Red Train').openPopup();
    L.marker([41.87551, -87.64244]).addTo(chicago_map).bindPopup("Blue Train").openPopup();
    L.marker([41.94702, -87.67474]).addTo(chicago_map).bindPopup('Brn Train').openPopup();
    L.marker([41.88422, -87.69623]).addTo(chicago_map).bindPopup('G Train').openPopup();
    L.marker([41.87695, -87.63365]).addTo(chicago_map).bindPopup('Pink Train').openPopup();
    L.marker([41.81249, -87.67968]).addTo(chicago_map).bindPopup('Org Train').openPopup();
    L.marker([42.02761, -87.6783]).addTo(chicago_map).bindPopup('P Train').openPopup();
    L.marker([0, 0]).addTo(chicago_map).bindPopup('Y Train').openPopup();
}

function send_data()
{
    document.getElementById("submit_data").onclick = function ()
    {
        var list_index = document.getElementById("train_list").selectedIndex;
        var get_trainName = document.getElementById("train_list").options;
      
       
       

      
       
    }


}