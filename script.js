// Example NFT data
const nftData = [
    { id: 1, title: "Abstract Colors", artist: "Artist XYZ", category: "art", image: "nft1.jpg" },
    { id: 2, title: "Neon Dreams", artist: "Artist ABC", category: "music", image: "nft2.jpg" },
    { id: 3, title: "Crypto Apes", artist: "Artist DEF", category: "apes", image: "nft3.jpg" },
    { id: 4, title: "Digital Collectible", artist: "Artist GHI", category: "collectibles", image: "nft4.jpg" },
  ];
  
  // Function to load NFT data
  function loadNFTs(filter = 'all') {
    const galleryGrid = document.getElementById("gallery-grid");
    galleryGrid.innerHTML = ""; // Clear existing NFTs
  
    // Filter and display NFTs
    const filteredNFTs = nftData.filter(nft => filter === 'all' || nft.category === filter);
    filteredNFTs.forEach(nft => {
      const nftCard = `
        <div class="nft-card">
          <img src="${nft.image}" alt="${nft.title}">
          <div class="nft-details">
            <h3>${nft.title}</h3>
            <p>by ${nft.artist}</p>
          </div>
        </div>`;
      galleryGrid.innerHTML += nftCard;
    });
  }
  
  // Event Listener for category filters
  function filterNFTs(category) {
    loadNFTs(category);
  }
  
  // Initial Load
  document.addEventListener("DOMContentLoaded", () => loadNFTs());
  

  // Select the button and gallery section
const exploreGalleryBtn = document.getElementById('exploreGalleryBtn');
const gallerySection = document.getElementById('gallerySection');

// Add event listener to button
exploreGalleryBtn.addEventListener('click', () => {
  // Toggle visibility of the gallery
  if (gallerySection.style.display === 'none' || gallerySection.style.display === '') {
    gallerySection.style.display = 'block';
    exploreGalleryBtn.textContent = "Hide Gallery"; // Optional: Change button text
  } else {
    gallerySection.style.display = 'none';
    exploreGalleryBtn.textContent = "Explore Gallery"; // Optional: Reset button text
  }
});
