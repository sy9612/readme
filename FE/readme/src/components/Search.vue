<template>
  <div id="Search">
    <div class="search-bar">
      <i class="fas fa-search"></i>
      <input type="text" class="search-input">
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'Search',

}
</script>

<style>
#Search {
  position: absolute;
  display: flex;
  flex-direction: column;
  background: #d7b9a1;
  box-sizing: border-box;
  top: 0;
  left: 0%;
  height: 100%;
  width: 100%;
  padding: 0 32%;
  padding-top: 10%;
}
.search-bar {
  position: relative;
  padding-left: 3%;
  top: 20%;
  height: 43px;
  border: 1px solid gray;
  border-radius: 24px;
  box-shadow: 2px 2px 2px 2px;
  outline: none;
}
/* .search-bar:hover {
  
} */
.search-input {
  position: relative;
  height: 94%;
  width: 70%;
  background: none;
  border: none;
  outline: none;
  border-radius: 24px;
  margin-left: 2%;
}
</style>