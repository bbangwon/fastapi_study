const fastapi = async (method, url, params = {}) => {
    let content_type = 'application/json';
    let body = JSON.stringify(params);

    let _url = import.meta.env.VITE_SERVER_UTL + url;
    if(method === 'get') {
        _url += '?' + new URLSearchParams(params).toString();        
    }
    
    let options = {
        method: method,
        headers: {
            'Content-Type': content_type,            
        }
    };

    if (method !== 'get') {
        options.body = body;
    }

    const response = await fetch(_url, options)    
    if(response.status === 204) { //no content
        return ''; 
    }

    const data = await response.json();
    if(response.status >= 200 && response.status < 300) {
        return data;
    }

    console.log(data);
    throw {status: response.status, statusText: response.statusText, error: data};
}

export default fastapi;