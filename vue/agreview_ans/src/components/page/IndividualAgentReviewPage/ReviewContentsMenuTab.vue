<script setup>
const emit = defineEmits(['select-tab'])

function selectTab(index){
    emit('select-tab', index)
}

</script>

<template>
    <div class = "navMenu">
        <nav>
            <ul>
                <li @click="selectTab(1)"><a href="#" >総合評価</a></li>
                <li><a href="#" @click="selectTab(2)">利用者口コミ</a></li>
                <li><a href="#" @click="selectTab(3)">口コミ投稿</a></li>
            </ul>
        </nav>
    </div>

</template>

<style scoped>

    nav ul li {
        display : inline-block;
        margin : 0 10px;
        width : 20%;
        background-color:rgb(220, 236, 245)
    }

    ul {
        margin:0
    }

    a {
        text-decoration: none;
    }

    nav li:hover{
        opacity: 0.8;
    }
    
</style>