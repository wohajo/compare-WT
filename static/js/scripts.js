var menuToggle = document.getElementById("menu-sidebar-toggle")
var menu = document.getElementById("menu-sidebar")
var comparsionTablesArray = document.getElementsByClassName('comparsion-table')
var countrySelectionArray = document.getElementsByClassName('country-comparsion-chooser')
var planeSelectionArray = document.getElementsByClassName('plane-comparsion-chooser')


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

function changePlaneSelection(planeChooser, comparsionTable) {
    planeId = planeChooser.value;

    fetch('/ple/' + planeId).then(function(response) {
        response.json().then(function(data) {
            name_ = data.plane.name
            imageLink = data.plane.img_link
            tier = data.plane.tier
            class_ = data.plane.class

            imageDiv = comparsionTable.getElementsByClassName('image-p')[0]
            nameDiv = comparsionTable.getElementsByClassName('name-p')[0]
            tierDiv = comparsionTable.getElementsByClassName('tier-p')[0]
            classDiv = comparsionTable.getElementsByClassName('class-p')[0]

            imageDiv.innerHTML = '<img src="' + imageLink + '" ' + 'alt="'+ name_ +'"></img>'
            nameDiv.innerHTML = name_
            tierDiv.innerHTML = tier
            classDiv.innerHTML = class_
        })
    })
}

function changeCountrySelection(countryChooser, planeChooser) {
    countryId = countryChooser.value;

    fetch('/co+pl/' + countryId).then(function(response) {
        response.json().then(function(data) {
            let optionHTML = ''
            for (let plane of data.planes) {
                optionHTML += '<option value="' + plane.id + '">' + plane.name + '</option>';
            }

            planeChooser.innerHTML = optionHTML
        })
    })
}

// shhhh! be quiet, they are listening

menuToggle.addEventListener("click", menuToggleClick)

countrySelectionArray[0].addEventListener("change", function() {changeCountrySelection(this, planeSelectionArray[0])});
countrySelectionArray[1].addEventListener("change", function() {changeCountrySelection(this, planeSelectionArray[1])});
countrySelectionArray[2].addEventListener("change", function() {changeCountrySelection(this, planeSelectionArray[2])});
countrySelectionArray[3].addEventListener("change", function() {changeCountrySelection(this, planeSelectionArray[3])});

planeSelectionArray[0].addEventListener("change", function() {changePlaneSelection(this, comparsionTablesArray[1])});
planeSelectionArray[1].addEventListener("change", function() {changePlaneSelection(this, comparsionTablesArray[2])});
planeSelectionArray[2].addEventListener("change", function() {changePlaneSelection(this, comparsionTablesArray[3])});
planeSelectionArray[3].addEventListener("change", function() {changePlaneSelection(this, comparsionTablesArray[4])});