import React, { useState } from 'react';

import './App.css'
import Topology from './topology.PNG'

import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
export default function Page() {



    const [openR1, setOpenR1] = React.useState(false);
    const [openR2, setOpenR2] = React.useState(false);
    const handleClickOpenR1 = () => {
        setOpenR1(true);
    };

    const handleCloseR1 = () => {
        setOpenR1(false);
    };

    const handleClickOpenR2 = () => {
        setOpenR2(true);
    };

    const handleCloseR2 = () => {
        setOpenR2(false);
    };
    const [R1Name, setR1Name] = useState("");
    const [R2Name, setR2Name] = useState("");


    // const handleR2Change = (event) => {
    //     setR2Name(event.target.value);
    // };

    const handleRouter1Name = (e) => {
        fetch(`http://localhost:8080/router1_name?name=${R1Name}`)
            .then(
                res => res.json()
            ).then(
                data => {
                    console.log(data.result)
                }
            )
    }

    const handleRouter1Config = (e) => {

        e.preventDefault()

        fetch("http://localhost:8080/router1_config")
            .then(
                res => res.json()
            ).then(
                data => {
                    console.log(data.result)
                }
            )

    }


    const clearRipRouter1 = (e) => {
        e.preventDefault()
        fetch(`http://localhost:8080/router1_clear`)
            .then(
                res => res.json()
            ).then(
                data => {
                    console.log(data.result)
                }
            )
    }

    const handleRouter2Name = (e) => {
        fetch(`http://localhost:8080/router2_name?name=${R2Name}`)
            .then(
                res => res.json()
            ).then(
                data => {
                    console.log(data.result)
                }
            )
    }

    const handleRouter2Config = (e) => {

        e.preventDefault()

        fetch("http://localhost:8080/router2_config")
            .then(
                res => res.json()
            ).then(
                data => {
                    console.log(data.result)
                }
            )

    }

    const clearRipRouter2 = (e) => {
        e.preventDefault()
        fetch(`http://localhost:8080/router2_clear`)
            .then(
                res => res.json()
            ).then(
                data => {
                    console.log(data.result)
                }
            )
    }

    return (


        <div className="page-container">
            <div className="App-header">
                <h1>RIP Configuration</h1>
            </div>
            <div className="content">
                <div className="buttonsplace" >

                    <div className="R-container">
                        <Button variant="outlined" className="buttonR1" onClick={handleClickOpenR1}>Changer Nom de Router 1</Button>
                        <Dialog

                            open={openR1} onClose={handleCloseR1}>

                            <DialogTitle>Changer Nom de Router 1</DialogTitle>

                            <DialogContent>
                                <form
                                    onSubmit={(e) => {

                                        handleRouter1Name(e)

                                    }}
                                >
                                    <DialogContentText>
                                        Pour changer le Nom click Confirmer et pour annuler click Annuler
                                    </DialogContentText>
                                    <TextField
                                        autoFocus
                                        margin="dense"
                                        id="name"
                                        label="Router Name"
                                        value={R1Name}
                                        fullWidth
                                        variant="standard"
                                        onChange={(e) => {
                                            setR1Name(e.target.value);
                                            // handleR2Change(R2);
                                        }}
                                    />
                                    <DialogActions>
                                        <Button onClick={handleCloseR1}>Annuler</Button>
                                        <Button type="submit"  >Confirmer </Button>
                                    </DialogActions>
                                </form>
                            </DialogContent>



                        </Dialog>


                        <Button sx={{
                            marginTop: 2
                        }}
                            variant="outlined" className="buttonR1" onClick={(e) => handleRouter1Config(e)} >Configurer Rip Router 1</Button>




                        <Button sx={{
                            marginTop: 2
                        }}
                            variant="outlined" className="buttonR1" onClick={(e) => clearRipRouter1(e)} >Clear Rip Router 1</Button>
                    </div>
                    {/*
                    R2 Router
                    */}


                    <div className="R-container">

                        <Button variant="outlined" className="buttonR1" onClick={handleClickOpenR2} >Changer Nom de Router 2</Button>

                        <Dialog
                            open={openR2} onClose={handleCloseR2}>
                            <DialogTitle>Changer Nom de Router 2</DialogTitle>
                            <DialogContent>
                                <form action=""
                                    onSubmit={(e) => {

                                        handleRouter2Name(e)

                                    }}

                                >
                                    <DialogContentText>
                                        Pour changer le Nom click Confirmer et pour annuler click Annuler

                                    </DialogContentText>
                                    <TextField
                                        name="R2"
                                        value={R2Name}
                                        autoFocus
                                        margin="dense"
                                        id="name"
                                        label="Router Name"
                                        fullWidth
                                        variant="standard"
                                        onChange={(e) => {
                                            setR2Name(e.target.value);
                                            // handleR2Change(R2);
                                        }}
                                    />
                                    <DialogActions>
                                        <Button onClick={handleCloseR2}>Cancel</Button>
                                        <Button type="submit">Confirmer</Button>
                                    </DialogActions>
                                </form>
                            </DialogContent>

                        </Dialog>

                        <Button
                            sx={{
                                marginTop: 2
                            }}
                            variant="outlined" className="buttonR1" onClick={(e) => handleRouter2Config(e)} >Configurer Rip Router 2</Button>


                        <Button sx={{
                            marginTop: 2
                        }}
                            variant="outlined" className="buttonR1" onClick={(e) => clearRipRouter2(e)}  >Clear Rip Router 2</Button>

                    </div>
                </div>
                <div className="imageplace">
                    <img src={Topology} alt="Logo" />
                </div>

            </div>

        </div>
    )
}
