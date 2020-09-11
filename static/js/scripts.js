var menuToggle = document.getElementById("menu-sidebar-toggle")
var menu = document.getElementById("menu-sidebar")
let country_select = document.getElementById('country')
let plane_select = document.getElementById('plane')

menuToggle.addEventListener("click", menuToggleClick)

function menuToggleClick() {
    menu.classList.toggle("sidebar--open")
    // TODO change hamburger icon to X
    // if (menu.style.width = 0) {
    //     menu.classList.add("sidebar--open")
    //     menuToggle.innerHTML = ("&times")
    // } else {
    //     menu.classList.remove("sidebar--open")
    //     menuToggle.innerHTML = ("&#9776")
    // }
}

country_select.onchange = function() {
    country_id = country_select.value;

    fetch('/co+pl/' + country_id).then(function(response) {
        response.json().then(function(data) {
            let optionHTML = ''
            for (let plane of data.planes) {
                optionHTML += '<option value="' + plane.id + '">' + plane.name + '</option>';
            }

            plane_select.innerHTML = optionHTML
        })
    })
}