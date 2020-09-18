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
            battleRatingAb = data.plane.battle_rating_ab
            battleRatingRb = data.plane.battle_rating_rb
            battleRatingSb = data.plane.battle_rating_sb
            crew = data.plane.crew
            takeOffWeight = data.plane.take_off_weight
            burstMass = data.plane.burst_mass
            noEngines = data.plane.no_engines
            engineType = data.plane.engine_type
            engineCoolingType = data.plane.engine_cooling_type
            engineName = data.plane.engine_name

            imageDiv = comparsionTable.getElementsByClassName('image-p')[0]
            nameDiv = comparsionTable.getElementsByClassName('name-p')[0]
            tierDiv = comparsionTable.getElementsByClassName('tier-p')[0]
            classDiv = comparsionTable.getElementsByClassName('class-p')[0]
            brAbDiv = comparsionTable.getElementsByClassName('battle-rating-ab-p')[0]
            brRbDiv = comparsionTable.getElementsByClassName('battle-rating-rb-p')[0]
            brSbDiv = comparsionTable.getElementsByClassName('battle-rating-sb-p')[0]
            crewDiv = comparsionTable.getElementsByClassName('crew-p')[0]
            takeOffWeightDiv = comparsionTable.getElementsByClassName('take-off-weight-p')[0]
            burstMassDiv = comparsionTable.getElementsByClassName('burst-mass-p')[0]
            noEnginesDiv = comparsionTable.getElementsByClassName('no-engines-p')[0]
            engineTypeDiv = comparsionTable.getElementsByClassName('engine-type-p')[0]
            engineCoolingTypeDiv = comparsionTable.getElementsByClassName('engine-cooling-type-p')[0]
            engineNameDiv = comparsionTable.getElementsByClassName('engine-name-p')[0]

            imageDiv.innerHTML = '<img src="' + imageLink + '" ' + 'alt="'+ name_ +'"></img>'
            nameDiv.innerHTML = name_
            tierDiv.innerHTML = tier
            classDiv.innerHTML = class_
            brAbDiv.innerHTML = battleRatingAb
            brRbDiv.innerHTML = battleRatingRb
            brSbDiv.innerHTML = battleRatingSb
            crewDiv.innerHTML = crew
            takeOffWeightDiv.innerHTML = takeOffWeight 
            burstMassDiv.innerHTML = burstMass
            noEnginesDiv.innerHTML = noEngines
            engineTypeDiv.innerHTML = engineType
            engineCoolingTypeDiv.innerHTML = engineCoolingType
            engineNameDiv.innerHTML = engineName
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