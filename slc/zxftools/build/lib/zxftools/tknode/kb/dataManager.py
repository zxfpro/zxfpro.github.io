from videodb import connect, play_stream
from videodb.timeline import Timeline
from llama_index.retrievers.videodb import VideoDBRetriever

class VideoDB:
    """
    """
    def __init__(self, api_key):
        self.conn = connect(api_key=api_key)
        self.retriever = VideoDBRetriever(api_key)
        self.timeline = Timeline(self.conn)

    def upload_video(self, url=None, file_path=None):
        #  video.get_transcript_text()
        if url:
            return self.conn.upload(url=url)
        elif file_path:
            return self.conn.upload(file_path=file_path)

    def index_spoken_words(self, video):
        video.index_spoken_words()

if __name__ == '__main__':

    # create video stream of search results
    conn = connect('sk-FlPdL0WJSwkBtZE8j6wT0XFr39QjGyNAeyEiJXBT9Mw')
    timeline = Timeline(conn)

    relevant_nodes = retriever.retrieve("What's the benefit of morning sunlight?")

    for node_obj in relevant_nodes:
        node = node_obj.node
        # create a video asset for each node
        node_asset = VideoAsset(
            asset_id=node.metadata["video_id"],
            start=node.metadata["start"],
            end=node.metadata["end"],
        )
        # add the asset to timeline
        timeline.add_inline(node_asset)

    # generate stream for the compiled timeline
    stream_url = timeline.generate_stream()
    play_stream(stream_url)