import CameraAltIcon from '@material-ui/icons/CameraAlt';
import DirectionsWalkIcon from '@material-ui/icons/DirectionsWalk';
import LocalMoviesIcon from '@material-ui/icons/LocalMovies';
import { Button, Card, CardActions, CardContent, CardHeader, CardMedia, IconButton, Typography } from "@mui/material";

const Post = () => {
  return (
    <Card sx={{ margin: 5 }}>
      <CardHeader />
      <CardMedia
        component="img"
        height="20%"
        image="https://images.pexels.com/photos/4534200/pexels-photo-4534200.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        alt="Paella dish"
      />
      <CardContent>
        <Typography variant="body2" color="text.secondary">
          BACK1
        </Typography>

      </CardContent>
        <CardActions>
            <Button size="small">EVENTS</Button>
            <Button size="small">RECORDINGS</Button>
        </CardActions>
      <CardActions disableSpacing>
        <IconButton aria-label="walk">
            <DirectionsWalkIcon />
        </IconButton>
        <IconButton aria-label="movie">
          <LocalMoviesIcon />
        </IconButton>
        <IconButton aria-label="cameras">
          <CameraAltIcon />
        </IconButton>
      </CardActions>
    </Card>
  );
};

export default Post;