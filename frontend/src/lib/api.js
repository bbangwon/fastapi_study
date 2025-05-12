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
    const data = await response.json();
    if(response.status >= 200 && response.status < 300) {
        return data;
    }
    else {
        throw new Error(`Response Status Error: ${response.status} ${response.statusText}`);
    }
}

export default fastapi;