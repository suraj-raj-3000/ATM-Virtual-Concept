
toggle = document.getElementById("toggle").className;
menu_toggle = document.getElementById("menu_toggle").className;
function toggle() {
    menu_toggle.classList.toggle('active');
}

theme_toggle = document.getElementById("theme_toggle").className;
theme_menu_toggle = document.getElementById("theme_menu_toggle").className;
function theme_toggle() {
    theme_menu_toggle.classList.toggle('active');
}

function toggle_(var1, var2) {
    home()
    var1.style.visibility = "hidden";
    var2.style.visibility = "visible";

}
function home() {
    middle_section.style.visibility = "visible";
    middle_section_withdraw.style.visibility = "hidden";
    middle_section_fund_transfer.style.visibility = "hidden";
    middle_section_cash_deposit.style.visibility = "hidden";
    middle_section_mini_statement.style.visibility = "hidden";
    middle_section_account.style.visibility = "hidden";
    middle_section_pin_change.style.visibility = "hidden";
    middle_section_card.style.visibility = "hidden";
}
function goBack() {
    window.history.back();
}

function ran() {
    document.getElementById('new_pin').value = Math.floor((Math.random() * 1000) + 1000);
}
// ================ Changing themes ===================

function theme(color) {
    if (color == 'dark') {
        document.getElementById("cont_f").style.background = 'linear-gradient(to bottom, #000000, #434343, #000000)';
        document.getElementById("menu1").style.background = '#1b1b1b';
        document.getElementById("menu2").style.background = '#1b1b1b';
        document.getElementById("menu_toggle").style.background = '#1b1b1b';
        document.getElementById("menu4").style.background = '#1b1b1b';
        document.getElementById("menu5").style.background = '#1b1b1b';
        document.getElementById("menu6").style.background = '#1b1b1b';
        document.getElementById("theme_menu_toggle").style.background = '#1b1b1b';
        document.getElementById("menu8").style.background = '#1b1b1b';

    } else if (color == 'blue') {
        document.getElementById("cont_f").style.background = 'linear-gradient(to bottom, #021a34, #053269, #021a34)';
        document.getElementById("menu1").style.background = '#0f70c0';
        document.getElementById("menu2").style.background = '#0f70c0';
        document.getElementById("menu_toggle").style.background = '#0f70c0';
        document.getElementById("menu4").style.background = '#0f70c0';
        document.getElementById("menu5").style.background = '#0f70c0';
        document.getElementById("menu6").style.background = '#0f70c0';
        document.getElementById("theme_menu_toggle").style.background = '#0f70c0';
        document.getElementById("menu8").style.background = '#0f70c0';

    } else if (color == 'red') {
        document.getElementById("cont_f").style.background = 'linear-gradient(to bottom, #200122, #6f0000, #200122)';
        document.getElementById("menu1").style.background = '#c5000a';
        document.getElementById("menu2").style.background = '#c5000a';
        document.getElementById("menu_toggle").style.background = '#c5000a';
        document.getElementById("menu4").style.background = '#c5000a';
        document.getElementById("menu5").style.background = '#c5000a';
        document.getElementById("menu6").style.background = '#c5000a';
        document.getElementById("theme_menu_toggle").style.background = '#c5000a';
        document.getElementById("menu8").style.background = '#c5000a';

    } else {

    }
}

// -------------- change language ------
function change_language(lang) {
    if (lang == 'india') {
        document.getElementById("home_text").innerHTML = "होम";
        document.getElementById("card_text").innerHTML = "कार्ड";
        document.getElementById("language_text").innerHTML = "भाषा";
        document.getElementById("back_text").innerHTML = "पीछे";
        document.getElementById("withdraw_text").innerHTML = "निकासी";
        document.getElementById("transfer_text").innerHTML = "ट्रांसफर";
        document.getElementById("cash_text").innerHTML = "नकद जमा";
        document.getElementById("mini_text").innerHTML = "मिनी स्टेटमेंट";
        document.getElementById("account_text").innerHTML = "बैंक खाता";
        document.getElementById("pin_text").innerHTML = "पिन चेंज";
        document.getElementById("cancel_text").innerHTML = "बंद करे";
        document.getElementById("themes_text").innerHTML = "थीम्स";
        document.getElementById("card_text").innerHTML = "कार्ड";
        document.getElementById("card_text").innerHTML = "कार्ड";
        document.getElementById("logout_text").innerHTML = "लॉग आउट";
    } else if (lang == 'english') {
        document.getElementById("home_text").innerHTML = "Home";
        document.getElementById("card_text").innerHTML = "Card";
        document.getElementById("language_text").innerHTML = "Language";
        document.getElementById("back_text").innerHTML = "Back";
        document.getElementById("withdraw_text").innerHTML = "Withdraw";
        document.getElementById("transfer_text").innerHTML = "transfer";
        document.getElementById("cash_text").innerHTML = "Deposit";
        document.getElementById("mini_text").innerHTML = "Mini Statement";
        document.getElementById("account_text").innerHTML = "Your Account";
        document.getElementById("pin_text").innerHTML = "PIN Change";
        document.getElementById("cancel_text").innerHTML = "Close";
        document.getElementById("themes_text").innerHTML = "Themes";
        document.getElementById("logout_text").innerHTML = "Log Out";
    } else if (lang == 'tamil') {
        document.getElementById("home_text").innerHTML = "வீடு";
        document.getElementById("card_text").innerHTML = "ஆட்டச்சீட்டு";
        document.getElementById("language_text").innerHTML = "மொழி";
        document.getElementById("back_text").innerHTML = "முதுகு";
        document.getElementById("withdraw_text").innerHTML = "பின்னிடு";
        document.getElementById("transfer_text").innerHTML = "இடமாற்றம்";
        document.getElementById("cash_text").innerHTML = "வைப்பு";
        document.getElementById("mini_text").innerHTML = "மினி அறிக்கை";
        document.getElementById("account_text").innerHTML = "வங்கிக் கணக்கு";
        document.getElementById("pin_text").innerHTML = "முள் மாற்றம்";
        document.getElementById("cancel_text").innerHTML = "அடைப்பு";
        document.getElementById("themes_text").innerHTML = "ஆய்வுப்பொருள்";
        document.getElementById("logout_text").innerHTML = "வெளியேறு";
    }

}