<script>
    import { onMount } from "svelte";
    import { EventCalendar } from "@dhx/trial-eventcalendar";
    import "@dhx/trial-eventcalendar/dist/event-calendar.css";
    import axios from 'axios';

    let events = [];
    let calendars = [];
    let date = new Date();  // Initialize with the current date
    let container;

    onMount(async () => {
        try {
            // Replace 'http://localhost:8000/api/' with your Django API base URL
            const eventsResponse = await axios.get('http://localhost:8000/api/events/');
            const calendarsResponse = await axios.get('http://localhost:8000/api/calendars/');
            
            events = eventsResponse.data;
            calendars = calendarsResponse.data;

            const calendar = new EventCalendar(container, {
                events,
                calendars,
                date
            });

            // Optional: setup RestDataProvider if needed
            // const url = 'http://localhost:8000/api/';
            // const restProvider = new eventCalendar.RestDataProvider(url);
            // calendar.api.setNext(restProvider);

        } catch (error) {
            console.error('Error fetching data:', error);
        }
    });
</script>

<div bind:this={container} style="width: 100%; height: 100%;"></div>
