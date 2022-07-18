import { Box, List, ListItem, ListItemButton, ListItemText } from "@mui/material";
import React from "react";

  
const Sidebar = ({mode,setMode}) => {
    return (
      <Box flex={1} p={2} sx={{ display: { xs: "none", sm: "block" } }}>
        <Box position="fixed">
          <List>
            <ListItem disablePadding>
              <ListItemButton component="a" href="#cameras">
                <ListItemText primary="Cameras" />
              </ListItemButton>
            </ListItem>
            <ListItem disablePadding>
              <ListItemButton component="a" href="#birdseye">
                <ListItemText primary="Birdseye" />
              </ListItemButton>
            </ListItem>
            <ListItem disablePadding>
              <ListItemButton component="a" href="#events">
                <ListItemText primary="Events" />
              </ListItemButton>
            </ListItem>
            <ListItem disablePadding>
              <ListItemButton component="a" href="#debug">
                <ListItemText primary="Debug" />
              </ListItemButton>
            </ListItem>
            
            <ListItem disablePadding>
              <ListItemButton component="a" href="#documentation">
                <ListItemText primary="Documentation" />
              </ListItemButton>
            </ListItem>
            <ListItem disablePadding>
              <ListItemButton component="a" href="#github">
                <ListItemText primary="Github" />
              </ListItemButton>
            </ListItem>
          </List>
        </Box>
      </Box>
    );
};
  
export default Sidebar;