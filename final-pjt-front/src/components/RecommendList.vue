<template>
    <div>

        이런 영화는 어떠세요?
        <div class="row d-flex justify-content-center p-3 mb-2 bg-dark">
            <RecommendListItem
            v-for="(RecommendPk, index) in movieCard.recommend"
            :key="index"
            :RecommendPk="RecommendPk"
            class="col-2 m-3"
            />
        </div>
    </div>
</template>

<script>
import RecommendListItem from '@/components/RecommendListItem'
export default {
    name: "RecommendList",
    components: {
        RecommendListItem,
    },
    props: {
        movieCard: Object,
    }
}
</script>

<style>

</style>