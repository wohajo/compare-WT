var menuToggle = document.getElementById("menu-sidebar-toggle")
var menu = document.getElementById("menu-sidebar")
let countrySelect = document.getElementById('country-comparsion-chooser-1')
let planeSelect = document.getElementById('plane-comparsion-chooser-1')

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

countrySelect.onchange = function() {
    countryId = countrySelect.value;

    fetch('/co+pl/' + countryId).then(function(response) {
        response.json().then(function(data) {
            let optionHTML = ''
            for (let plane of data.planes) {
                optionHTML += '<option value="' + plane.id + '">' + plane.name + '</option>';
            }

            planeSelect.innerHTML = optionHTML
        })
    })
}

planeSelect.onchange = function() {
    planeId = planeSelect.value;

    fetch('/ple/' + planeId).then(function(response) {
        response.json().then(function(data) {
            console.log(data)
            nameDiv = document.getElementsByClassName('comparsion-table')[1].getElementsByClassName('name-p')[0]
            nameHTML = data.plane.name
            nameDiv.innerHTML = nameHTML
        })
    })
}