var container = document.getElementById("container");
var addButton = document.getElementById("addButton");
var confirmButton = document.getElementById("confirmButton");

var configContent1 = "微信";
var configContent2 = "/desktop/default";

function createNewElement(addContent) {
  var newElement = document.createElement("div");
  newElement.style.display = "flex";
  newElement.style.justifyContent = "center";

  var inputElement1 = document.createElement("input");
  inputElement1.classList.add("input");
  inputElement1.style.width = "40px";
  inputElement1.type = "text";
  inputElement1.placeholder = "名称";
  if (addContent) {
    inputElement1.value = configContent1;
  }

  var inputElement2 = document.createElement("input");
  inputElement2.classList.add("input");
  inputElement2.style.width = "180px";
  inputElement2.type = "text";
  inputElement2.placeholder = "路径";
  if (addContent) {
    inputElement2.value = configContent2;
  }

  var buttonElement = document.createElement("button");
  buttonElement.innerHTML = "✘";
  buttonElement.classList.add("deleteBtn");
  buttonElement.addEventListener("click", function () {
    newElement.parentNode.removeChild(newElement);
  });

  newElement.appendChild(inputElement1);
  newElement.appendChild(inputElement2);
  newElement.appendChild(buttonElement);

  return newElement;
}

function addNewElement(addContent) {
  var newElement = createNewElement(addContent);
  container.appendChild(newElement);
}

//模拟添加已有的名称&路径
addNewElement(true);
configContent1="QQ"
configContent2="/blah"
addNewElement(true);

//点击添加新的名称&路径
addButton.addEventListener("click", function () {
  addNewElement(false);
});

confirmButton.addEventListener("click", function () {
  var elements = container.querySelectorAll("div");
  var content = "";

  for (var i = 0; i < elements.length; i++) {
    var inputElements = elements[i].querySelectorAll("input");
    var inputValue1 = inputElements[0].value;
    var inputValue2 = inputElements[1].value;
    content += inputValue1 + " " + inputValue2 + "\n";
  }

  // var link = document.createElement("a");
  // link.href = "data:text/plain;charset=utf-8," + encodeURIComponent(content);
  // link.download = "namepath.txt";
  // link.style.display = "none";
  // document.body.appendChild(link);
  // link.click();
  // document.body.removeChild(link);
});
