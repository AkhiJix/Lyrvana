$( "#target" ).submit(function( event ) {
    // prevent default behaviour
    event.preventDefault();
    // clear results list
    document.getElementById("srList").innerHTML = "";
    // get form values
    var searchQuery = $("#search").val();
    document.getElementById("srA").innerHTML = searchQuery;
    var radioButtonOption = $('input[name=cat]:checked').val();

    var matchParams;
    if(radioButtonOption == 1 ) {
        matchParams = {artist: (searchQuery)};
        document.getElementById("srCat").innerHTML = "artist";
    }
    else if(radioButtonOption == 2) {
        matchParams = {songname: (searchQuery)};
        document.getElementById("srCat").innerHTML = "song name";
    }
    else if(radioButtonOption == 3) {
        matchParams = {lyrics: (searchQuery)};
        document.getElementById("srCat").innerHTML = "lyrics containing";
    }
    // create a client with jQuery build
    var client = new $.es.Client({
        host: 'https://elastic:CcrIUTedTbLYCZyEqHVKfYmQ@7e4e69552436e5c164c62ed7afb082a8.us-west-2.aws.found.io:9243'
    });

    // search the client for results
    client.search({
        index: 'lyrvanaindex',
        body: {
            query: {
                match: matchParams
            }
        }
    }).then(function (resp) {
//        console.log(resp);
        document.getElementById("srN").innerHTML = resp.hits.total;
        document.getElementById("srT").innerHTML = resp.took;
        document.getElementById("sr").style.display = "block";

        // console.log(resp.hits.hits)
        for(var i=0;i<resp.hits.hits.length;i++){
            var artistImage = resp.hits.hits[i]._source.artist.replace(/ /g,"_");;
            // console.log(artistImage)
            var newUL = document.createElement("li");
            newUL.classList.add("row");
//            newUL.innerHTML = resp.hits.hits[i]._source;
            var newUL2 =
            '                            <div class="col s2" style="padding:0px">\n' +
            '                                <img alt="Artist Image" src="images/artists/'+artistImage+'.jpg" alt="" class="responsive-img"> <!-- notice the "circle" class -->\n' +
            '                            </div>\n' +
            '                            <div class="col s10" style="position:relative;padding-top:0px;margin:0px;">\n' +
            '                                <h5>'+resp.hits.hits[i]._source.artist+'</h5>\n' +
            '                                <h6>'+resp.hits.hits[i]._source.songname+'</h6>\n' +
            '                                <p class="truncate">'+resp.hits.hits[i]._source.lyrics+'</p>\n' +
            '                                <p class="chip white-text" style="position:absolute;top:0px;right:10px;background-color: #1db954">'+(resp.hits.hits[i]._score)+'</p>\n '+
            '                            </div>\n' +
            '                        ';
            newUL.innerHTML = newUL2;
            document.getElementById("srList").append(newUL);
        }


    }, function (err) {
        console.trace(err.message);
    });

});