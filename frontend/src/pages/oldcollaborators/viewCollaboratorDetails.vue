<template>
  <div>
    User {{ $route.params.id }}
    <ul>
      <li>Contact information</li>
      <li>Photo</li>
      <li>Events data</li>
      <li>Media links</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "viewCollaboratorDetails"
};
</script>

<style>
</style>