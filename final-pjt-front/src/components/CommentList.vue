<template>
  <div class="comment-box">
    <CommentListItem
      @delete-comment="deleteComment"
      v-for="(comment, index) in comments"
      :key="index"
      :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from "@/components/CommentListItem";

export default {
  name: "CommentList",
  components: {
    CommentListItem,
  },
  props: {
    movieCard: Object,
    comments: Array,
  },
  computed: {
    nowComments() {
      return this.comments;
    },
  },
  methods: {
    deleteComment(id) {
      const nowComments = this.nowComments;
      const index = nowComments.findIndex((obj) => obj.id == id);
      nowComments.splice(index, 1);
    },
  },
};
</script>

<style scoped>
.comment-box {
  display: block;
  width: 50%;
  height: 100%;

  margin: 0 auto;
  justify-content: center;
}
</style>
