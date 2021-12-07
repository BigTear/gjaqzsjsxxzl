//clear the input 
function clearInput() {
    $("#keywords").val("");
}

function format(obj) {
    //format json object to str
    var str = JSON.stringify(obj);
    //remove null in str
    str = str.replace(/null/g, "");
    //remove '{', '}' in str
    str = str.replace(/{/g, "");
    str = str.replace(/}/g, "");
    //replace '",' to '<br>' in str
    str = str.replace(/",/g, "<br>");
    str = str.replace(/",/g, "");
    //replace 'option_a' to 'A' in str
    str = str.replace(/"option_a/g, "A");
    str = str.replace(/"option_b/g, "B");
    str = str.replace(/"option_c/g, "C");
    str = str.replace(/"option_d/g, "D");
    str = str.replace(/"option_e/g, "E");
    str = str.replace(/"option_f/g, "F");
    str = str.replace(/"option_g/g, "G");

    str = str.replace(/"id/g, "id");
    str = str.replace(/"question/g, "问题");
    str = str.replace(/"answer/g, "答案");
    //replace '":"' to '：' in str
    str = str.replace(/":"/g, "：");

    str = str.replace(/E":,F":,G":,/g, "");
    str = str.replace(/<br>E：<br>F：<br>G："/g, "");

    return str;
}

function searchQue() {
    //refresh the p tag
    $("#show").html("");
    keyword = $("#keywords").val();
    if (keyword == "") {
        return;
    }
    //which one quetype radio button is checked, then get its value
    var quetype = $("#quetype").val();
    for (var i = 0; i < quetype.length; i++) {
        if (quetype[i].checked) {
            quetype = quetype[i].value;
            break;
        }
    }
    filename = quetype + '.json';
    $.getJSON(filename, function (jsonData) {
        for (var i = 0; i < jsonData.length; i++) {
            if (jsonData[i]['question'].indexOf(keyword) >= 0) {
                //add formated json to existed p tag which id is show
                document.getElementById("show").innerHTML += format(jsonData[i]) + 
                    '<br/>' + '='.repeat(20) + '<br/>';
            }
        }
    })

}