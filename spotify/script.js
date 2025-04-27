document.addEventListener('DOMContentLoaded', () => {
    const artistsData = [
        {name: 'Bathory', image: './img/banda-bathory.png' },
        {name: 'Crystal Castles', image: './img/banda-crystalcastles.png' },
        {name: 'Death', image: './img/banda-death.png' },
        {name: 'Sepultura', image: './img/banda-sepultura.png' },
        {name: 'Crypta', image: './img/banda-crypta.png' },
        {name: 'Lana Del Rey', image: './img/cantora-lana.png' }
    ];
    
    const albunsData = [
        {name: 'Arise', artist: 'Sepultura', image: './img/album-arise.png' },
        {name: 'Abyss', artist: 'Pastel Ghost', image: './img/album-abyss.png' },
        {name: 'Around the Fur', artist: 'Deftones',  image: './img/album-atf.png' },
        {name: 'Cowboys From Hell', artist: 'Pantera', image: './img/album-cfh.png' },
        {name: 'Ride The Lightning', artist: 'Metallica', image: './img/album-rtl.png' },
        {name: 'Left Hand Path', artist: 'Entombed',image: './img/album-lhp.png' }
    ];

    const artistGrid = document.querySelector('.artists-grid')
    const albunsGrid = document.querySelector('.albums-grid')

    artistsData.forEach( artist => {
        const artistCard = document.createElement('div')
        artistCard.classList.add('artist-card')

        artistCard.innerHTML = `
            <img src="${artist.image}" alt="imagem do ${artist.name}">
            <div>
                <h3>${artist.name}</h3>
                <p>artista</p>
            </div>
        `

        artistGrid.appendChild(artistCard)
    })

    albunsData.forEach( album => {
        const albumCard = document.createElement('div')
        albumCard.classList.add('album-card')

        albumCard.innerHTML = `
            <img src="${album.image}" alt="imagem do ${album.name}">
            <div>
                <h3>${album.name}</h3>
                <p>${album.artist}</p>
            </div>
        
        `

        albunsGrid.appendChild(albumCard)
    })
})


