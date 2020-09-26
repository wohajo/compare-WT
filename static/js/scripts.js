var menuToggle = document.getElementById("menu-sidebar-toggle")
var menu = document.getElementById("menu-sidebar")
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
        return "<img src='static/images/check-no-icon-24.png' alt='no'>"
    }
    else if (value == '1' || value == 1) {
        return "<img src='static/images/check-yes-icon-24.png' alt='yes'>"
    }
    else {
        return "N/A"
    }
}

function changePlaneSelection(planeChooser, number) {
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

            noEngines = checkIfNull(data.plane.no_engines)
            engineType = checkIfNull(data.plane.engine_type)
            engineCoolingType = checkIfNull(data.plane.engine_cooling_type)
            engineName = checkIfNull(data.plane.engine_name)
            engineBasePower = checkIfNull(data.plane.base_power)
            engineWEPPower = checkIfNull(data.plane.wep_power)

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
            
            combatFlaps = checkBool(data.plane.combat_flaps)
            takeOffFlaps = checkBool(data.plane.take_off_flaps)
            landingFlaps = checkBool(data.plane.landing_flaps)
            // airBrakes = checkBool(data.plane.air_brakes)
            // arrestorGear = checkBool(data.plane.arrestor_gear) 
            // drogueChute = checkBool(data.plane.drogue_chute) 
            // radarWarningReceiver = checkBool(data.plane.radar_warning_receiver) 
            // ballisticComputer = checkBool(data.plane.ballistic_computer)
            modules = checkIfNull(data.plane.modules)

            sodStructural = checkIfNull(data.plane.sod_structural)
            sodGear = checkIfNull(data.plane.sod_gear)
            sodCombatFlaps = checkIfNull(data.plane.sod_combat_flaps)
            sodTakeoffFlaps = checkIfNull(data.plane.sod_takeoff_flaps)
            sodLandingFlaps = checkIfNull(data.plane.sod_landing_flaps)

            ailerons = checkIfNull(data.plane.ailerons)
            rudder = checkIfNull(data.plane.rudder)
            elevators = checkIfNull(data.plane.elevators)
            radiator = checkIfNull(data.plane.radiator)

            offArm = checkIfNull(data.plane.offensive_armament)
            defArm = checkIfNull(data.plane.defensive_armament)
            susArm = checkIfNull(data.plane.suspended_armament)

            imageDiv = document.getElementsByClassName('image-p')[number]
            nameDiv = document.getElementsByClassName('name-p')[number]
            tierDiv = document.getElementsByClassName('tier-p')[number]
            classDiv = document.getElementsByClassName('class-p')[number]
            brAbDiv = document.getElementsByClassName('battle-rating-ab-p')[number]
            brRbDiv = document.getElementsByClassName('battle-rating-rb-p')[number]
            brSbDiv = document.getElementsByClassName('battle-rating-sb-p')[number]
            crewDiv = document.getElementsByClassName('crew-p')[number]
            takeOffWeightDiv = document.getElementsByClassName('take-off-weight-p')[number]
            burstMassDiv = document.getElementsByClassName('burst-mass-p')[number]
            engineDiv = document.getElementsByClassName('engine-p')[number]
            engineBasePowerDiv = document.getElementsByClassName('engine-base-power-p')[number]
            engineWEPPowerDiv = document.getElementsByClassName('engine-wep-power-p')[number] 
            
            isPremiumDiv = document.getElementsByClassName('is-premium-p')[number]
            researchDiv = document.getElementsByClassName('research-p')[number]
            purchaseDiv = document.getElementsByClassName('purchase-p ')[number]
            repairMinAbDiv = document.getElementsByClassName('repair-min-ab-p')[number]
            repairMaxAbDiv = document.getElementsByClassName('repair-max-ab-p')[number]
            repairMinRbDiv = document.getElementsByClassName('repair-min-rb-p')[number]
            repairMaxRbDiv = document.getElementsByClassName('repair-max-rb-p')[number]
            repairMinSbDiv = document.getElementsByClassName('repair-min-sb-p')[number]
            repairMaxSbDiv = document.getElementsByClassName('repair-max-sb-p')[number]
            crewTrainingDiv = document.getElementsByClassName('crew-training-p')[number]
            expertsDiv = document.getElementsByClassName('experts-p')[number]
            acesDiv = document.getElementsByClassName('aces-p')[number]
            rewardRpDiv = document.getElementsByClassName('reward-rp-p')[number]
            rewardSlSbDiv = document.getElementsByClassName('reward-sl-ab-p')[number]
            rewardSlRbDiv = document.getElementsByClassName('reward-sl-rb-p')[number]
            rewardSlAbDiv = document.getElementsByClassName('reward-sl-sb-p')[number]

            maxSpeedStockAbDiv = document.getElementsByClassName('max-speed-stock-ab-p')[number]
            maxSpeedUpgradedAbDiv = document.getElementsByClassName('max-speed-upgraded-ab-p')[number]
            maxSpeedStockRbDiv = document.getElementsByClassName('max-speed-stock-rb-p')[number]
            maxSpeedUpgradedRbDiv = document.getElementsByClassName('max-speed-upgraded-rb-p')[number]
            maxAltDiv = document.getElementsByClassName('max-alt-p')[number]
            turnStockAbDiv = document.getElementsByClassName('turn-stock-ab-p')[number]
            turnUpgradedAbDiv = document.getElementsByClassName('turn-upgraded-ab-p')[number]
            turnStockRbDiv = document.getElementsByClassName('turn-stock-rb-p')[number]
            turnUpgradedRbDiv = document.getElementsByClassName('turn-upgraded-rb-p')[number]
            rocStockAbDiv = document.getElementsByClassName('roc-stock-ab-p')[number]
            rocUpgradedAbDiv = document.getElementsByClassName('roc-upgraded-ab-p')[number]
            rocStockRbDiv = document.getElementsByClassName('roc-stock-rb-p')[number]
            rocUpgradedRbDiv = document.getElementsByClassName('roc-upgraded-rb-p')[number]
            takeOffRunDiv = document.getElementsByClassName('take-off-run-p')[number]
            
            combatFlapsDiv = document.getElementsByClassName('combat-flaps-p')[number]
            takeOffFlapsDiv = document.getElementsByClassName('take-off-flaps-p')[number]
            landingFlapsDiv = document.getElementsByClassName('landing-flaps-p')[number]
            // TODO make some icons for commented
            // airBrakesDiv = document.getElementsByClassName('air-brakes-p')[number]
            // arrestorGearDiv = document.getElementsByClassName('arrestor-gear-p')[number]
            // drogueChuteDiv = document.getElementsByClassName('drogue-chute-p')[number]
            // radarWarningReceiverDiv = document.getElementsByClassName('radar-warning-receiver-p')[number]
            // ballisticComputerDiv = document.getElementsByClassName('ballistic-computer-p')[number]
            modulesDiv = document.getElementsByClassName('modules-p')[number]

            sodStructuralDiv = document.getElementsByClassName('sod-structural-p')[number]
            sodGearDiv = document.getElementsByClassName('sod-gear-p')[number]
            sodCombatFlapsDiv = document.getElementsByClassName('sod-combat-flaps-p')[number]
            sodTakeoffFlapsDiv = document.getElementsByClassName('sod-takeoff-flaps-p')[number]
            sodLandingFlapsDiv = document.getElementsByClassName('sod-landing-flaps-p')[number]

            aileronsDiv = document.getElementsByClassName('ailerons-p')[number]
            rudderDiv = document.getElementsByClassName('rudder-p')[number]
            elevatorsDiv = document.getElementsByClassName('elevators-p')[number]
            radiatorDiv = document.getElementsByClassName('radiator-p')[number]

            offArmDiv = document.getElementsByClassName('offensive-armament-p')[number]
            defArmDiv = document.getElementsByClassName('defensive-armament-p')[number]
            susArmDiv = document.getElementsByClassName('suspended-armament-p')[number]

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

            engineDiv.innerHTML = noEngines + " x " + engineName + " (" + engineType + ")" 
            engineBasePowerDiv.innerHTML = engineBasePower
            engineWEPPowerDiv.innerHTML = engineWEPPower

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

            combatFlapsDiv.innerHTML = combatFlaps 
            takeOffFlapsDiv.innerHTML = takeOffFlaps 
            landingFlapsDiv.innerHTML = landingFlaps 
            // airBrakesDiv.innerHTML = airBrakes 
            // arrestorGearDiv.innerHTML = arrestorGear 
            // drogueChuteDiv.innerHTML = drogueChute 
            // radarWarningReceiverDiv.innerHTML = radarWarningReceiver 
            // ballisticComputerDiv.innerHTML = ballisticComputer
            modulesDiv.innerHTML = modules

            sodStructuralDiv.innerHTML = sodStructural
            sodGearDiv.innerHTML = sodGear
            sodCombatFlapsDiv.innerHTML = sodCombatFlaps
            sodTakeoffFlapsDiv.innerHTML = sodTakeoffFlaps
            sodLandingFlapsDiv.innerHTML = sodLandingFlaps

            aileronsDiv.innerHTML = ailerons
            rudderDiv.innerHTML = rudder
            elevatorsDiv.innerHTML = elevators
            radiatorDiv.innerHTML = radiator

            offArmDiv.innerHTML = offArm
            defArmDiv.innerHTML = defArm
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

changePlaneSelection(planeSelectionArray[0], 0)
changePlaneSelection(planeSelectionArray[1], 1)
changePlaneSelection(planeSelectionArray[2], 2)
changePlaneSelection(planeSelectionArray[3], 3)

menuToggle.addEventListener("click", menuToggleClick)

countrySelectionArray[0].addEventListener("change", function() {changeCountrySelection(this, planeSelectionArray[0])});
countrySelectionArray[1].addEventListener("change", function() {changeCountrySelection(this, planeSelectionArray[1])});
countrySelectionArray[2].addEventListener("change", function() {changeCountrySelection(this, planeSelectionArray[2])});
countrySelectionArray[3].addEventListener("change", function() {changeCountrySelection(this, planeSelectionArray[3])});

planeSelectionArray[0].addEventListener("change", function() {changePlaneSelection(this, 0)});
planeSelectionArray[1].addEventListener("change", function() {changePlaneSelection(this, 1)});
planeSelectionArray[2].addEventListener("change", function() {changePlaneSelection(this, 2)});
planeSelectionArray[3].addEventListener("change", function() {changePlaneSelection(this, 3)});


