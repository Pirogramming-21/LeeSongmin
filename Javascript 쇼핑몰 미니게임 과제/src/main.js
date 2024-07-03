
// Fetch the items from the JSON file
function loadItems() {
    return fetch('data/data.json') // 브라우저 api인 fetch를 이용해서 데이터 받아옴.
    .then(response => response.json()) // 1. fetch는 데이터를 성공적으로 받아오면 response라는 object를 전달 2. response의 body를 json의 object로 변환
    .then(json => json.items);
}

// Update the list with the given items
function displayItems(items) {
    const container = document.querySelector('.items');
    container.innerHTML =  items.map(item => createHTMLString(item)).join('');
    // Json의 items를 html요소(li 태그)로 변환
    // 한 가지의 배열 형태를 다른 형태의 배열로 변환 : map(a => b) 이용
    // 문자열이 들어있는 배열을 한 가지의 큰 문자열로 병합 : join()
}

// Create HTML list item from the given data item
function createHTMLString(item) {
    return `
    <li class="item">
          <img src="${item.image}" alt="${item.type}" class="item__thumbnail" />
          <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `
    // String 템플릿: ``
    // ``: ''랑 다른거임. ~ 키보드에 같이
}

// main
loadItems() //item을 동적으로 받아옴
    .then(items => { //promise를 리턴. promise가 성공적으로 되면 items 받아오도록 함.
        //console.log(items); // 확인용
        displayItems(items); //HTML에 items를 보여줌
        //setEventListeners(items); //버튼을 클릭했을 때 적절히 필터링
    })
    .catch(console.log)