let codes = document.querySelectorAll("code")
// console.log(codes)
let formats = [
  // [new RegExp(/gap>/), 'pink'],
  // [new RegExp(/if/), 'green'],
  // [new RegExp(/while/), 'red'],
  // [new RegExp(/for/), 'orange'],

  // [new RegExp(/:=/), 'blue'],
  // [new RegExp(/===/), 'blue'],
  // [new RegExp(/!==/), 'blue'],
  // [new RegExp(/==/), 'blue'],
  // [new RegExp(/!=/), 'blue'],
  // [new RegExp(/=/), 'blue'],
  // [new RegExp(/>=/), 'blue'],
  // [new RegExp(/<=/), 'blue'],
  // [new RegExp(/>/), 'blue'],
  // [new RegExp(/</), 'blue'],

  // [/;/, 'yellow'],
  // [/quit/, 'red'],


  // [/\+/, 'red'],
  // [/\//, 'red'],
  // [/\-/, 'red'],
  // [/\*/, 'red'],
  // [new RegExp(/[A-Za-z][a-zA-Z0-9]+/), 'green'],
  ['gap>', 'pink'],
  ['if', '#78dce8'],
  ['while', '#78dce8'],
  ['for', '#78dce8'],
  ['else', '#78dce8'],
  ['od', '#78dce8'],
  ['of', '#78dce8'],
  ['do', '#78dce8'],
  ['then', '#78dce8'],
  ['in', '#78dce8'],

  [':=', '#fd6086'],
  ['===', '#fd6086'],
  ['!==', '#fd6086'],
  ['==', '#fd6086'],
  ['!=', '#fd6086'],
  ['=', '#fd6086'],
  ['>=', '#fd6086'],
  ['<=', '#fd6086'],
  ['>', '#fd6086'],
  ['<', '#fd6086'],
  ['[', '#fd6086'],
  [']', '#fd6086'],
  [',', '#fd6086'],

  [';', 'yellow'],
  ['quit', 'red'],


  ['+', '#fd6086'],
  ['/', '#fd6086'],
  ['-', '#fd6086'],
  ['*', '#fd6086h'],

  [';', '#fdf9f3'],
  ['(', '#908e8f'],
  [')', '#908e8f'],
]

String.prototype.regexIndexOf = function(regex, startpos) {
  var indexOf = this.substring(startpos || 0).search(regex);
  return (indexOf >= 0) ? (indexOf + (startpos || 0)) : indexOf;
}

String.prototype.regexLastIndexOf = function(regex, startpos) {
  regex = (regex.global) ? regex : new RegExp(regex.source, "g" + (regex.ignoreCase ? "i" : "") + (regex.multiLine ? "m" : ""));
  if(typeof (startpos) == "undefined") {
    startpos = this.length;
  } else if(startpos < 0) {
    startpos = 0;
  }
  var stringToWorkWith = this.substring(0, startpos + 1);
  var lastIndexOf = -1;
  var nextStop = 0;
  while((result = regex.exec(stringToWorkWith)) != null) {
    lastIndexOf = result.index;
    regex.lastIndex = ++nextStop;
  }
  return lastIndexOf;
}

function getMinMax(arr) {
  for(let i=0;i<arr.length;i++) {
    if(arr[i] === -1) {
      delete arr[i]
    }
  }
  return arr.reduce(({min, max}, v) => ({
    min: min < v ? min : v,
    max: max > v ? max : v,
  }), { min: arr[0], max: arr[0] });
}

function decodeHTMLContent(htmlText) {
  var txt = document.createElement("span");
  txt.innerHTML = htmlText;
  return txt.innerText;
}

function colorise(data) {
  let keys = []
  data = decodeHTMLContent(data)
  // console.log(data)
  let min = 0
  for(let i = 0; i<=20; i++) {
    // console.log(data)
    let indexs = []
    for(let j=0;j<formats.length;j++) {
      let ind = data.indexOf(formats[j][0])
      indexs.push(ind)
      if(ind !== -1) {
        // console.log(ind)
        // console.log(formats[j])
      }
    }
    // console.log(indexs)
    let checks = getMinMax(indexs)
    // console.log(checks)
    if(checks.min !== undefined) {
      min = checks.min
      let k = indexs.indexOf(checks.min)
      // console.log(k)
      // console.log(formats[k])
     let pref_a = '<span style="color:'+ formats[k][1] +';">'
     let pref_b = '</span>'
     let a = data.substr(0, checks.min)
     let b = data.substr(checks.min + formats[k][0].length)
     keys.push(a + pref_a + formats[k][0] + pref_b)
     data = b
    }
  }
  if(data != "") {
    keys.push(data)
  }
  // console.log(keys)
  return keys.join('')
  // return data
}

for(let i=0; i<codes.length; i++) {
  let data = codes[i].innerHTML

  data = colorise(data)

  // let index = []
  // while(true) {
  //  let isMin = undefined
  //  let isMinIndex = undefined
  //  for(let j=0;j<formats.length;j++) {
  //    let ind = data.indexOf(formats[j][0])
  //    if(ind !== -1) {
  //      if(isMin === undefined) {
  //        isMin = ind
  //        isMinIndex = j
  //      }
  //      else if(ind < isMin) {
  //        isMin = ind
  //        isMinIndex = j
  //      }
  //      index.push([ j, ind ])
  //    }
  //  }
  //  console.log(index)
  //  console.log(isMin)
  //  // if(formats[isMinIndex] || formats[isMinIndex][0]) {
  //  //  continue
  //  // }
  //  if(isMinIndex !== undefined) {
  //    console.log(isMinIndex)
  //    console.log(formats[isMinIndex])
  //    console.log(formats[isMinIndex][0])
  //    a = data.substr(0, isMin)
  //    console.log(a)
  //    b = data.substr(isMin + formats[isMinIndex][0].length)
  //    console.log(b)

  //    let pref_a = '<font color="'+ formats[isMinIndex][1] +'">'
  //    let pref_b = '</font>'
  //    data = a + pref_a + formats[isMinIndex][0] + pref_b + b
  //    isMinIndex += pref_a.length + pref_b.length
  //  }
  //  else {
  //    break;
  //  }
  // }

  // data = data.replace('if', '<font color="green">if</font>')
  // data = data.replace('while', '<font color="green">while')
  // data = data.replace('for', '<font color="green">for</font>')
  // data = data.replace('==', '<font color="orange">==</font>')
  // data = data.replace(':=', '<font color="orange">:=</font>')
  // data = data.replace(':=', '<font color="orange">:=</font>')
  // // console.log(data)
  codes[i].innerHTML = data
  // break
}
