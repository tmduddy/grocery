getMealPlanList()
getRecipeList()
getIngredientList()

function getMealPlanList() {
    const wrapper = document.querySelector('#mealplan-list-wrapper')
    
    const baseUrl = "http://127.0.0.1:5050/api/food/";
    const mealplanUrl = baseUrl + 'meal_plan/'
    let options = {method: 'GET'}
    fetch(mealplanUrl, options)
        .then((resp) => resp.json())
        .then((data) => {
            console.log(data)
            for (let i in data) {
                var item = `
                    <div id="data-row-${i}" class="mealplan-wrapper flex-wrapper item-wrapper">
                        <div style="flex:7">
                            <span class="name">${data[i].name}</span>
                        </div>
                    </div>
                `
                wrapper.innerHTML += item
            }
        })
}

function getRecipeList() {
    const wrapper = document.querySelector('#recipe-list-wrapper')
    
    const baseUrl = "http://127.0.0.1:5050/api/food/";
    const recipeUrl = baseUrl + 'recipe/'
    let options = {method: 'GET'}
    fetch(recipeUrl, options)
        .then((resp) => resp.json())
        .then((data) => {
            console.log(data)
            for (let i in data) {
                var item = `
                    <div id="data-row-${i}" class="recipe-wrapper flex-wrapper item-wrapper">
                        <div style="flex:7">
                            <span class="name">${data[i].name}</span>
                        </div>
                    </div>
                `
                wrapper.innerHTML += item
            }
        })
}

function getIngredientList() {
    const wrapper = document.querySelector('#ingredient-list-wrapper')
    
    const baseUrl = "http://127.0.0.1:5050/api/food/";
    const ingredientUrl = baseUrl + 'ingredient/'
    let options = {method: 'GET'}
    fetch(ingredientUrl, options)
        .then((resp) => resp.json())
        .then((data) => {
            wrapper.innerHTML = ''
            for (let i in data) {
                var item = `
                    <div id="data-row-${i}" class="ingredient-wrapper flex-wrapper item-wrapper">
                        <div style="flex:7">
                            <span class="name">${data[i].name}</span>
                        </div>
                    </div>
                `
                wrapper.innerHTML += item
            }
        })
}

function toggleMealplan() {
    document.querySelector('#container-mealplan').setAttribute('style', '')
    document.querySelector('#container-recipe').setAttribute('style', 'display:none')
    document.querySelector('#container-ingredient').setAttribute('style', 'display:none')
}

function toggleRecipe() {
    document.querySelector('#container-mealplan').setAttribute('style', 'display:none')
    document.querySelector('#container-recipe').setAttribute('style', '')
    document.querySelector('#container-ingredient').setAttribute('style', 'display:none')
}

function toggleIngredient() {
    document.querySelector('#container-mealplan').setAttribute('style', 'display:none')
    document.querySelector('#container-recipe').setAttribute('style', 'display:none')
    document.querySelector('#container-ingredient').setAttribute('style', '')
}

const recipeSubmit = document.querySelector('#recipe-form-wrapper')
recipeSubmit.addEventListener('submit', function(e) {
    e.preventDefault()
    const data = document.querySelector("#recipe-name").value
    const baseUrl = "http://127.0.0.1:5050/api/food/";
    const recipeUrl = baseUrl + 'recipe/';
    const options = {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({'name': data})
    }
    fetch(recipeUrl, options).then(function() {
        getRecipeList()
        console.log(options)
    })
})


const ingredientSubmit = document.querySelector('#ingredient-form-wrapper')
ingredientSubmit.addEventListener('submit', function(e) {
    e.preventDefault()
    const data = document.querySelector("#ingredient-name").value
    const baseUrl = "http://127.0.0.1:5050/api/food/";
    const ingredientUrl = baseUrl + 'ingredient/';
    const options = {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({'name': data})
    }
    fetch(ingredientUrl, options).then(function(resp) {
        getIngredientList()
        document.querySelector('#form-ingredient').reset()
    })
})


