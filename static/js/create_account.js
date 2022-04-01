var numbersOnly = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;

loadFile = function(event) {

	var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};

function populate(b1, b2) {

    

    var b1 = document.getElementById(b1);
    var b2 = document.getElementById(b2);

    var d = new Date();
    var year = d.getFullYear();
    var month = d.getMonth();
    var day = d.getDate();

    var e = new Date(year + 10, month, day);
    var c = e.toLocaleDateString("en-IN");


    if (b1.value == "Patna") {
        document.create_form.ifsc_code_box.value = "BKID0005814";
        document.create_form.account_no.value = Math.floor((Math.random() * 1000) + 581410110001000);
        document.create_form.atm_no.value = Math.floor((Math.random() * 1000000) + 6069980068729498);
        document.create_form.cvv.value = Math.floor((Math.random() * 100) + 100);
        document.create_form.showDate.value = c;
    }
    else if (b1.value == "Jamui") {
        document.create_form.ifsc_code_box.value = "BKID0002519";
        document.create_form.account_no.value = Math.floor((Math.random() * 1000) + 581410110001000);
        document.create_form.atm_no.value = Math.floor((Math.random() * 1000000) + 6069980068729498);
        document.create_form.cvv.value = Math.floor((Math.random() * 100) + 100);
        document.create_form.showDate.value = c;
    }
    else if (b1.value == "select") {
        document.create_form.ifsc_code_box.value = "";
        document.create_form.account_no.value = "";
        document.create_form.atm_no.value = "";
        document.create_form.cvv.value = "";
        document.create_form.showDate.value = "";
    }


}


function stringvalidation(objid,ermssgid){
    var objid = document.forms["create_form"][objid];
    var er_mssg_id = document.getElementById(ermssgid);
    if (objid.value == "") {
        er_mssg_id.innerHTML = "Fields must be filled out *";
        return false;
    } else {
        er_mssg_id.innerHTML = "";
    }
}


function validateForm() {
    // Select Branch validation ----
    if (document.getElementById('select_branch').value == "select") {
        document.getElementById('select_branch_msg').innerHTML = "Select Branch *";
        alert("Some fields are blank");
        return false;
    } else {
        document.getElementById('select_branch_msg').innerHTML = "";
    }
    // full name validation ----
    if(document.forms["create_form"]["fname"].value == "") {
        document.getElementById('name_error').innerHTML = "Please enter your name.";
        alert("Please Fill your full name.");
        return false;
    } else {
        document.getElementById('father_name_error').innerHTML = "";
    }
    
    // father name validation ----
    if (document.forms["create_form"]["father_name"].value == "") {
        document.getElementById('father_name_error').innerHTML = "Father's name must be filled out *";
        alert("Father's name can't be empty");
        return false;
    } else {
        document.getElementById('father_name_error').innerHTML = "";
    }

    // Mother name validation ----
    if (document.forms["create_form"]["mother_name"].value == "") {
        document.getElementById('mother_name_error').innerHTML = "Mother's name must be filled out *";
        alert("Mother's name can't be empty");
        return false;
    } else {
        document.getElementById('mother_name_error').innerHTML = "";
    }
    
    // gender validation ------------
    var radios = document.getElementsByName("gender_radio_btn");
    var gendervalid = false;

    var i = 0;
    while (!gendervalid && i < radios.length) {
        if (radios[i].checked) gendervalid = true;
        i++;
    }

    if (!gendervalid) {
        // document.getElementById('gender_error').innerHTML = "Must select gender option!";
        alert("Select Your Gender.");
        return false;
    }

    // marrage validation ------------
    var m_radios = document.getElementsByName("married_radio_btn");
    var marragevalid = false;

    var j = 0;
    while (!marragevalid && j < m_radios.length) {
        if (m_radios[i].checked) marragevalid = true;
        j++;
    }

    if (!marragevalid) {
        // document.getElementById('marrage_error').innerHTML = "Must select gender option!";
        alert("Select Your Marital Status.");
        return false;
    }
    
    // Phone number validation ----
    if (document.forms["create_form"]["phone_number"].value == "") {
        document.getElementById('phone_number_error').innerHTML = "Phone number must be filled out *";
        alert("Phone number can't be empty.");
        return false;
    } else {
        document.getElementById('phone_number_error').innerHTML = "";
    }

    // Pan number validation ----
    if (document.forms["create_form"]["pan_number"].value == "") {
        document.getElementById('pan_number_error').innerHTML = "PAN number must be filled out *";
        alert("PAN number can't be empty.");
        return false;
    } else {
        document.getElementById('pan_number_error').innerHTML = "";
    }

    // Email validation ----
    if (document.forms["create_form"]["email"].value == "") {
        document.getElementById('email_error').innerHTML = "Email must be filled out *";
        alert("Email can't be empty.");
        return false;
    } else {
        document.getElementById('email_error').innerHTML = "";
    }

    // Id proof validation ----
    if (document.forms["create_form"]["id_proof"].value == "Identity Proof *") {
        document.getElementById('id_proof_error').innerHTML = "Select Id Proof.";
        alert("Id proof must be selected.");
        return false;
    } else {
        document.getElementById('id_proof_error').innerHTML = "";
    }

    // Id proof number validation ----
    if (document.forms["create_form"]["id_proof_number"].value == "") {
        document.getElementById('id_proof_number_error').innerHTML = "Enter Id proof number *";
        alert("Id proof number must be entered.");
        return false;
    } else {
        document.getElementById('id_proof_number_error').innerHTML = "";
    }

    // Address validation ----
    if (document.forms["create_form"]["address"].value == "") {
        document.getElementById('address_error').innerHTML = "Enter your Current Address.";
        alert("Address must be filled out.");
        return false;
    } else {
        document.getElementById('address_error').innerHTML = "";
    }
    
    // State validation ----
    if (document.forms["create_form"]["inputState"].value == "Select State .. *") {
        document.getElementById('state_error').innerHTML = " Please select State?";
        alert("State must be Selected *");
        return false;
    } else {
        document.getElementById('state_error').innerHTML = "";
    }

    // District validation----
    if (document.forms["create_form"]["dist"].value == "") {
        document.getElementById('dist_error').innerHTML = " Please enter District?";
        alert("District must be Filled out! *");
        return false;
    } else {
        document.getElementById('dist_error').innerHTML = "";
    }

    // PIN Code validation----
    if (document.forms["create_form"]["pin_code"].value == "") {
        document.getElementById('pin_code_error').innerHTML = " Please enter PIN code ?";
        alert("Pin Code must be Filled out! *");
        return false;
    } else {
        document.getElementById('pin_code_error').innerHTML = "";
    }

    // PIN Code validation----
    if (document.forms["create_form"]["user_photo"].value == "") {
        // document.getElementById('pin_code_error').innerHTML = " Please enter PIN code ?";
        alert("Select photo! *");
        return false;
    } else {
        // document.getElementById('pin_code_error').innerHTML = "";
    }

}
    // --------------Nominee validation ------------
function nomi_visi_false(){
    var nomi_radios = document.getElementById("Nominee_radio_btn").value;
    if (nomi_radios == "no"){
        document.getElementById("nomi_details_box").style.visibility = "hidden";
        document.getElementById("nomi_address_details_box").style.visibility = "hidden";
        document.getElementById("term_condition").style.marginTop = "-120px";
    }
}

function nomi_visi_yes(){
    var nomi_radio_yes = document.getElementById("Nominee_radio_btn_yes").value;
    if(nomi_radio_yes == "yes"){
        document.getElementById("nomi_details_box").style.visibility = "visible";
        document.getElementById("nomi_address_details_box").style.visibility = "visible";
        document.getElementById("term_condition").style.marginTop = "0px";

  
    }
}
// ------------ to valodate number -------------



function validatePhoneNumber(input_str) {
    var re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;

    return re.test(input_str);
}

function validatenumber() {
    var phone = document.getElementById('phone_number').value;
    if (!validatePhoneNumber(phone)) {
        document.getElementById('phone_number_error').innerHTML="Enter currect mobile number";
    } else {
        document.getElementById('phone_number_error').innerHTML="";
    }
}
