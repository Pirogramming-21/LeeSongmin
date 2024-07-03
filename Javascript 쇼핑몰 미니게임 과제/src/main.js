
// Fetch the items from the JSON file
function loadItems() {
    return fetch('data/data.json') // 브라우저 api인 fetch를 이용해서 데이터 받아옴.
    .then(response => response.json()) // 1. fetch는 데이터를 성공적으로 받아오면 response라는 object를 전달 2. response의 body를 json의 object로 변환
    .then(json => json.items);
}

// main
loadItems() //item을 동적으로 받아옴
    .then(items => { //promise를 리턴. promise가 성공적으로 되면 items 받아오게
        //displayItems(items); //HTML에 items를 보여줌
        //setEventListeners(items); //버튼을 클릭했을 때 적절히 필터링
    })
    .catch(console.log)