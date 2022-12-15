const lswitch = document.querySelector("#light-switch")
lswitch.addEventListener('click',()=>{
    const light = document.querySelector('.container')
    if (lswitch.innerText === 'Turn On Lights') {
        light.classList.add('lights')
        lswitch.innerText = 'Turn Off Lights'
    }else{
        light.classList.remove('lights')
        lswitch.innerText = 'Turn On Lights'
    }
})