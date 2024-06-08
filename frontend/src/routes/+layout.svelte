<script>
    export const prerender = true;
    import Navbar from './Navbar/+page.svelte';
</script>

<svelte:head>
    <link href="https://fonts.google.com/specimen/Do+Hyeon?subset=korean&noto.script=Kore" rel="stylesheet">
    <style>
        body {
            font-family: 'Do Hyeon', sans-serif;
        }
    </style>
</svelte:head>
<Navbar />
<slot></slot>