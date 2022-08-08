
def index():
    return '''
    <h2>RESTApi Equipment Communication Application</h2>
    <h4>Here are a list of endpoints:</h4>
    <ul>
        <li>Queue</li>
        <ul>
            <li><a href="/queue/get">Fetch Queue</a></li>
            <li><a href="/queue/post">Post Queue</a></li>
        </ul>
        <li>Equipment</li>
        <ul>
            <li><a href="/equip/get">Fetch Equipment</a></li>

        </ul>
    </ul>
    '''