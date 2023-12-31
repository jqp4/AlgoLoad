"use strict";

/** Модель загрузки данных. */
class DataLoader {
    static emptyGraphDataTemplate = { vertices: [], edges: [] };

    constructor() {
        this.graphData = DataLoader.emptyGraphDataTemplate;
    }

    async loadGraphData() {
        const href = window.location.href; // http://localhost:3001/user/q000/AlgoViewPage.html
        const mainPath = href.slice(0, href.lastIndexOf("/")); // http://localhost:3001/user/q000
        const jsonGraphDataUrl = mainPath + "/Json_models/graphData.json"; // http://localhost:3001/user/d000/Json_models/graphData.json

        let rawData = "";

        await $.ajax({
            type: "GET",
            url: jsonGraphDataUrl,
            headers: { "cache-control": "no-cache" }, // !!!
            success: function (data) {
                console.log("data from ajax.get = ", data);
                rawData = data;
            },
        });

        this.graphData = rawData;
        return this.graphData;
    }
}
