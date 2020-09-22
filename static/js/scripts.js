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

function checkIfNull(value) {
    if (value != null) {
        return value
    } else {
        return "N/A"
    }
}

function checkBool(value) {
    if (value == '0' || value == 0) {
        return "no"
    }
    else if (value == '1' || value == 1) {
        return "yes"
    }
    else {
        return "N/A"
    }
}

function changePlaneSelection(planeChooser, comparsionTable) {
    planeId = planeChooser.value;

    fetch('/ple/' + planeId).then(function(response) {
        response.json().then(function(data) {

            name_ = checkIfNull(data.plane.name)
            imageLink = checkIfNull(data.plane.img_link)
            tier = checkIfNull(data.plane.tier)
            class_ = checkIfNull(data.plane.class)
            battleRatingAb = checkIfNull(data.plane.battle_rating_ab)
            battleRatingRb = checkIfNull(data.plane.battle_rating_rb)
            battleRatingSb = checkIfNull(data.plane.battle_rating_sb)
            crew = checkIfNull(data.plane.crew)
            takeOffWeight = checkIfNull(data.plane.take_off_weight)
            burstMass = checkIfNull(data.plane.burst_mass)
            noEngines = checkIfNull(data.plane.no_engines)
            engineType = checkIfNull(data.plane.engine_type)
            engineCoolingType = checkIfNull(data.plane.engine_cooling_type)
            engineName = checkIfNull(data.plane.engine_name)
            
            isPremium = checkBool(data.plane.is_premium)
            research = checkIfNull(data.plane.research)
            purchase = checkIfNull(data.plane.purchase)
            repairMinAb = checkIfNull(data.plane.repair_min_ab)
            repairMaxAb = checkIfNull(data.plane.repair_max_ab)
            repairMinRb = checkIfNull(data.plane.repair_min_rb)
            repairMaxRb = checkIfNull(data.plane.repair_max_rb)
            repairMinSb = checkIfNull(data.plane.repair_min_sb)
            repairMaxSb = checkIfNull(data.plane.repair_max_sb)
            crewTraining = checkIfNull(data.plane.crew_training)
            experts = checkIfNull(data.plane.experts)
            aces = checkIfNull(data.plane.aces)
            rewardRp = checkIfNull(data.plane.reward_rp)
            rewardSlSb = checkIfNull(data.plane.reward_sl_sb)
            rewardSlRb = checkIfNull(data.plane.reward_sl_rb)
            rewardSlAb = checkIfNull(data.plane.reward_sl_ab)

            maxSpeedStockAb = checkIfNull(data.plane.max_speed_stock_ab)
            maxSpeedUpgradedAb = checkIfNull(data.plane.max_speed_upgraded_ab)
            maxSpeedStockRb = checkIfNull(data.plane.max_speed_stock_rb)
            maxSpeedUpgradedRb = checkIfNull(data.plane.max_speed_upgraded_rb)
            maxAlt = checkIfNull(data.plane.max_alt)
            turnStockAb = checkIfNull(data.plane.turn_stock_ab)
            turnUpgradedAb = checkIfNull(data.plane.turn_upgraded_ab)
            turnStockRb = checkIfNull(data.plane.turn_stock_rb)
            turnUpgradedRb = checkIfNull(data.plane.turn_upgraded_rb)
            rocStockAb = checkIfNull(data.plane.roc_stock_ab)
            rocUpgradedAb = checkIfNull(data.plane.roc_upgraded_ab)
            rocStockRb = checkIfNull(data.plane.roc_stock_rb)
            rocUpgradedRb = checkIfNull(data.plane.roc_upgraded_rb)
            takeOffRun = checkIfNull(data.plane.take_off_run)

            susArm = checkIfNull(data.plane.suspended_armament)

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
            
            isPremiumDiv = comparsionTable.getElementsByClassName('is-premium-p')[0]
            researchDiv = comparsionTable.getElementsByClassName('research-p')[0]
            purchaseDiv = comparsionTable.getElementsByClassName('purchase-p ')[0]
            repairMinAbDiv = comparsionTable.getElementsByClassName('repair-min-ab-p')[0]
            repairMaxAbDiv = comparsionTable.getElementsByClassName('repair-max-ab-p')[0]
            repairMinRbDiv = comparsionTable.getElementsByClassName('repair-min-rb-p')[0]
            repairMaxRbDiv = comparsionTable.getElementsByClassName('repair-max-rb-p')[0]
            repairMinSbDiv = comparsionTable.getElementsByClassName('repair-min-sb-p')[0]
            repairMaxSbDiv = comparsionTable.getElementsByClassName('repair-max-sb-p')[0]
            crewTrainingDiv = comparsionTable.getElementsByClassName('crew-training-p')[0]
            expertsDiv = comparsionTable.getElementsByClassName('experts-p')[0]
            acesDiv = comparsionTable.getElementsByClassName('aces-p')[0]
            rewardRpDiv = comparsionTable.getElementsByClassName('reward-rp-p')[0]
            rewardSlSbDiv = comparsionTable.getElementsByClassName('reward-sl-ab-p')[0]
            rewardSlRbDiv = comparsionTable.getElementsByClassName('reward-sl-rb-p')[0]
            rewardSlAbDiv = comparsionTable.getElementsByClassName('reward-sl-sb-p')[0]

            maxSpeedStockAbDiv = comparsionTable.getElementsByClassName('max-speed-stock-ab-p')[0]
            maxSpeedUpgradedAbDiv = comparsionTable.getElementsByClassName('max-speed-upgraded-ab-p')[0]
            maxSpeedStockRbDiv = comparsionTable.getElementsByClassName('max-speed-stock-rb-p')[0]
            maxSpeedUpgradedRbDiv = comparsionTable.getElementsByClassName('max-speed-upgraded-rb-p')[0]
            maxAltDiv = comparsionTable.getElementsByClassName('max-alt-p')[0]
            turnStockAbDiv = comparsionTable.getElementsByClassName('turn-stock-ab-p')[0]
            turnUpgradedAbDiv = comparsionTable.getElementsByClassName('turn-upgraded-ab-p')[0]
            turnStockRbDiv = comparsionTable.getElementsByClassName('turn-stock-rb-p')[0]
            turnUpgradedRbDiv = comparsionTable.getElementsByClassName('turn-upgraded-rb-p')[0]
            rocStockAbDiv = comparsionTable.getElementsByClassName('roc-stock-ab-p')[0]
            rocUpgradedAbDiv = comparsionTable.getElementsByClassName('roc-upgraded-ab-p')[0]
            rocStockRbDiv = comparsionTable.getElementsByClassName('roc-stock-rb-p')[0]
            rocUpgradedRbDiv = comparsionTable.getElementsByClassName('roc-upgraded-rb-p')[0]
            takeOffRunDiv = comparsionTable.getElementsByClassName('take-off-run-p')[0]

            susArmDiv = comparsionTable.getElementsByClassName('sus-arm-p')[0]

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
            
            isPremiumDiv.innerHTML = isPremium
            researchDiv.innerHTML = research
            purchaseDiv.innerHTML = purchase
            repairMinAbDiv.innerHTML = repairMinAb
            repairMaxAbDiv.innerHTML = repairMaxAb
            repairMinRbDiv.innerHTML = repairMinRb
            repairMaxRbDiv.innerHTML = repairMaxRb
            repairMinSbDiv.innerHTML = repairMinSb
            repairMaxSbDiv.innerHTML = repairMaxSb
            crewTrainingDiv.innerHTML = crewTraining
            expertsDiv.innerHTML = experts
            acesDiv.innerHTML = aces
            rewardRpDiv.innerHTML = rewardRp
            rewardSlSbDiv.innerHTML = rewardSlSb
            rewardSlRbDiv.innerHTML = rewardSlRb
            rewardSlAbDiv.innerHTML = rewardSlAb

            maxSpeedStockAbDiv.innerHTML = maxSpeedStockAb
            maxSpeedUpgradedAbDiv.innerHTML = maxSpeedUpgradedAb
            maxSpeedStockRbDiv.innerHTML = maxSpeedStockRb
            maxSpeedUpgradedRbDiv.innerHTML = maxSpeedUpgradedRb
            maxAltDiv.innerHTML = maxAlt
            turnStockAbDiv.innerHTML = turnStockAb
            turnUpgradedAbDiv.innerHTML = turnUpgradedAb
            turnStockRbDiv.innerHTML = turnStockRb
            turnUpgradedRbDiv.innerHTML = turnUpgradedRb
            rocStockAbDiv.innerHTML = rocStockAb
            rocUpgradedAbDiv.innerHTML = rocUpgradedAb
            rocStockRbDiv.innerHTML = rocStockRb
            rocUpgradedRbDiv.innerHTML = rocUpgradedRb
            takeOffRunDiv.innerHTML = takeOffRun

            susArmDiv.innerHTML = susArm
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
// #f1de2acf yellow
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