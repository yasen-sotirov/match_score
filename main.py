from fastapi import FastAPI
from routers.users import users_router
from routers.admins import admins_router
from routers.players import players_router
from routers.admin_requests import admin_requests_router
from routers.director_requests import director_requests_router
from routers.matches import matches_router
from routers.tournaments import tournaments_router
from routers.statistics import statistics_router
from routers.teams import teams_router


app = FastAPI(title='Match Score', description='Organization and management app of sport events.')
app.include_router(users_router)
app.include_router(admins_router)
app.include_router(players_router)
app.include_router(admin_requests_router)
app.include_router(director_requests_router)
app.include_router(teams_router)
app.include_router(matches_router)
app.include_router(tournaments_router)
app.include_router(statistics_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)


# uvicorn main:app